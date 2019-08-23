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
from random import randint

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
    
# Count up timers and burn cards
def count_timers(rlist):
    timers = 0
    burns = 0
    for item in rlist:
        if 'TIMER' in item:
            timers = timers + 1
        if 'BURN' in item:
            burns = burns + 1
    return timers, burns
        
def build_deck(burn, timer, total):
    timer_deck = []

    for i in range(timer):
        timer_deck.append('TIMER')
        
    for i in range(burn):
        timer_deck.append('TIMER, BURN')
        
    for i in range(total - (burn + timer)):
        timer_deck.append('ELEMENT')

    return timer_deck

# Experimenting with a variant where timers are added
# between each stage
def add_timers(burn, timer, rlist):
    for i in range(burn):
        rlist.append('TIMER, BURN')
        
    for i in range(timer):
        rlist.append('TIMER')
        
    return rlist

# This is somewhat of a guess, but 1-2 seems the most common number,
# fewer encounters means the game will tend to last longer, but
# it also means you can't do as much
encounter_distribution = [0, 1, 1, 1, 2, 2, 2, 2, 2, 2]

add_burn_cards = 2
add_timer_cards = 0

burn_cards = 6
timer_cards = 4
total_cards = 20

# 4,3,2,1=10, 3,2,2,2=9

sample_deck = build_deck(burn_cards, timer_cards, total_cards)
tcards, bcards = count_timers(sample_deck)
print('Timers', tcards, '/', len(sample_deck), '(', bcards, 'burn )', encounter_distribution)

# Number of trials to gather results    
epochs = 10000

# Number of stages in the game
stages = 3

# Number of triggers in each stage
num_triggers = [1, 2, 3]

# Number of timers per stage
num_timers = [3, 3, 3]

# Holds the number of turns for each stage
turns_dict = {}

# Holds whether the deck emptied out
empty_deck_dict = {}
    
# See how each stage looks
for stage in range(stages):
    turns_dict[stage] = []
    empty_deck_dict[stage] = []

# Iterate a number of epochs
for e in range(epochs):

    # Reset the deck
    timer_deck = build_deck(burn_cards, timer_cards, total_cards)
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
            for i in range(num_triggers[stage]):
                if current_card < len(timer_deck):
                    card = timer_deck[current_card]
                    if 'TIMER' in card:
                        timers = True
                current_card = current_card + 1
                
            if timers:
                timer = timer + 1
                
            # Did it go over the total number of timers?
            if timer >= num_timers[stage]:
                break
            
            encounters = encounter_distribution[randint(0,9)]
            
            # Encounters
            for i in range(encounters):
                if current_card < len(timer_deck):
                    card = timer_deck[current_card]
                    if 'BURN' in card:
                        timer_deck.pop(current_card)
                    else:
                        current_card = current_card + 1
        
        timer_deck = add_timers(add_burn_cards, add_timer_cards, timer_deck)
                
        if timer < num_timers[stage]:
            empty_deck_dict[stage].append(1)
        else:
            empty_deck_dict[stage].append(0)
            
        turns_dict[stage].append(turns)
        
prev_avg = 0

for i in range(stages):
    cur_avg = sum(turns_dict[i]) / len(turns_dict[i])
    percent_empty = sum(empty_deck_dict[i]) / len(empty_deck_dict[i])
    print('stage: ', i, ' turns: ', round(cur_avg, 3), ' diff: ', round(cur_avg - prev_avg, 3), ' stdev: ', round(statistics.stdev(turns_dict[i]), 3), 'empty: ', round(percent_empty, 4))
    prev_avg = cur_avg