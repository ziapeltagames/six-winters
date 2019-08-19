# -*- coding: utf-8 -*-
"""
A script to determine the average number and variance of turns 
in a game of Six Winters. Experiment with varying the size of the
encounter deck and the number of timers in the encounter deck,
as well as looking at the effect of having different numbers of
encounters.

Created on Sun Aug 18 16:46:05 2019

@author: zia
"""

from random import shuffle
import statistics

# Remove the item with the given string from the list
def remove_bysubs(rlist, rsubstring):

    rindex = 0
    for next_string in rlist:
        if rsubstring in next_string:
            break
        rindex = rindex + 1
    rlist.pop(rindex)
    return rlist    
    
def build_deck():
    timer_deck = []

    timer_deck.append('TIMER,BURN')
    timer_deck.append('TIMER,BURN')
    timer_deck.append('TIMER,BURN')
    timer_deck.append('TIMER,BURN')
    timer_deck.append('TIMER,BURN')
    timer_deck.append('TIMER,BURN')
    timer_deck.append('TIMER,BURN')

    timer_deck.append('TIMER,BURN')
    timer_deck.append('TIMER,BURN')
    timer_deck.append('TIMER,BURN')

    timer_deck.append('EARTH')
    timer_deck.append('EARTH')
    timer_deck.append('EARTH')
    timer_deck.append('EARTH')
    timer_deck.append('AIR')
    timer_deck.append('AIR')
    timer_deck.append('AIR')
    timer_deck.append('WATER')
    timer_deck.append('WATER')
    timer_deck.append('FIRE')

    return timer_deck

# Number of trials to gather results    
epochs = 100000

# Number of stages in the game
stages = 3

# Number of timers per stage
num_timers = 3

# Number of encounters each turn
# encounters_list = [0,1,2,3]
encounters_list = [1, 2, 3]

# Holds the number of turns for each stage
turns_dict = {}

# See how the results look for different numbers of encounters
for encounters in encounters_list:
    
    # See how each stage looks
    for stage in range(stages):
        turns_dict[stage] = []
    
    for e in range(epochs):
    
        # Reset the deck
        timer_deck = build_deck()
        turns = 0
        
        for stage in range(stages):
            
            timer = 0
            shuffle(timer_deck)
            
            # During each stage, go through the deck
            current_card = 0
            
            # If the deck runs out, the stage is also done
            while current_card < len(timer_deck):
                turns = turns + 1
                
                # If any triggers are a timer, add to the timer total
                timers = False
                for i in range(stage + 1):
                    if current_card < len(timer_deck):
                        card = timer_deck[current_card]
                        if 'TIMER' in card:
                            timers = True
                    current_card = current_card + 1
                    
                if timers:
                    timer = timer + 1
                    
                # Did it go over the total number of timers?
                if timer >= num_timers:
                    break
                
                # Encounters
                for i in range(encounters):
                    if current_card < len(timer_deck):
                        card = timer_deck[current_card]
                        if 'BURN' in card:
                            timer_deck.pop(current_card)
                        else:
                            current_card = current_card + 1
                
            turns_dict[stage].append(turns)
            
    prev_avg = 0
    
    print('Encounters: ',encounters)
    
    for i in range(stages):
        cur_avg = sum(turns_dict[i]) / len(turns_dict[i])
        print('stage: ',i,' turns: ',round(cur_avg, 2),' diff: ',round(cur_avg - prev_avg, 2),' stdev: ',round(statistics.stdev(turns_dict[i]), 2))
        prev_avg = cur_avg