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
    
    return timers
        
def build_deck(burn, timer, trigger):
    timer_deck = []

    for i in range(timer):
        timer_deck.append('TIMER')
        
    for i in range(burn):
        timer_deck.append('TIMER, BURN')

    for i in range(trigger):
        timer_deck.append('ELEMENT')

        
    # for i in range(total - (burn + timer)):
    #     timer_deck.append('ELEMENT')

    return timer_deck

def build_threat_deck(mil, dip, arc, esp, trade):
    threat_deck = []
    
    for i in range(mil):
        threat_deck.append('MIL '+str(i+1))
        
    for i in range(dip):
        threat_deck.append('DIP'+str(i+1))
        
    for i in range(arc):
        threat_deck.append('ARC'+str(i+1))
        
    for i in range(esp):
        threat_deck.append('ESP'+str(i+1))
        
    for i in range(trade):
        threat_deck.append('TRADE')
        
    return threat_deck
        
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
encounter_distribution = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3]

add_burn_cards = 2
add_timer_cards = 0

burn_cards = 12
timer_cards = 8
trigger_cards = 20

# 4,3,2,1=10, 3,2,2,2=9

sample_deck = build_deck(burn_cards, timer_cards, trigger_cards)
tcards = count_timers(sample_deck)
print('Timers', tcards, '/', len(sample_deck), '(', burn_cards, 'burn )', encounter_distribution)

# Number of trials to gather results    
epochs = 15000

# Number of stages in the game
stages = 3

# How many campaign cards to draw
campaign_cards = 2

# Number of triggers in each stage
num_triggers = [1, 2, 3]

# Number of timers per stage
num_timers = [3, 3, 3]

# Holds the number of turns for each stage
turns_dict = {}

# Holds how many timers are in the deck after each stage
timer_dict = {}

# Holds whether the deck emptied out
empty_deck_dict = {}
    
mil_threat_list = []
mil_val_list = []

# See how each stage looks
for stage in range(stages):
    turns_dict[stage] = []
    timer_dict[stage] = []
    empty_deck_dict[stage] = []

# Iterate a number of epochs
for e in range(epochs):

    # Reset the deck
    timer_deck = build_deck(burn_cards, timer_cards, trigger_cards)
    threat_deck = build_threat_deck(6,6,6,6,4)
    
    current_threat_card = 0
    mil_threats = 0
    mil_vals = 0
    shuffle(threat_deck)
    
    turns = 0
    
    for stage in range(stages):
        
        timer = 0
        shuffle(timer_deck)
        
        # During each stage, go through the deck
        current_card = 0
        
        # If the deck runs out, the stage is also done
        while current_card < len(timer_deck):
            turns = turns + 1
            
            # Draw a threat card
            # for i in range(campaign_cards):
            #     if current_threat_card < len(threat_deck):
            #         threat_card = threat_deck[current_threat_card]
            #         if 'MIL' in threat_card:
            #             mil_threats = mil_threats + 1
            #             mil_vals = mil_vals + int(threat_card[-1:])
            #         current_threat_card = current_threat_card + 1
            
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
        
        # timer_deck = add_timers(add_burn_cards, add_timer_cards, timer_deck)
                
        if timer < num_timers[stage]:
            empty_deck_dict[stage].append(1)
        else:
            empty_deck_dict[stage].append(0)
            
        turns_dict[stage].append(turns)
        
        tl = count_timers(timer_deck)
        timer_dict[stage].append(tl)
        
        mil_threat_list.append(mil_threats)
        mil_val_list.append(mil_vals)
        
prev_avg = 0

for i in range(stages):
    
    cur_avg = sum(turns_dict[i]) / len(turns_dict[i])
    percent_empty = float(sum(empty_deck_dict[i])) / float(len(empty_deck_dict[i]))
    avg_timers = sum(timer_dict[i]) / len(timer_dict[i])
    
    print('stage: ', i, ' turns: ', round(cur_avg, 3), ' diff: ', round(cur_avg - prev_avg, 3), ' stdev: ',
          round(statistics.stdev(turns_dict[i]), 3), ' empty: ', round(percent_empty, 4),
          ' timer:', round(avg_timers, 4))
    prev_avg = cur_avg
    
# mil_avg = sum(mil_threat_list) / len(mil_threat_list)
# mil_val_avg = sum(mil_val_list) / len(mil_val_list)
# print('Threat: ', round(mil_avg, 3), statistics.stdev(mil_threat_list), round(mil_val_avg, 3))