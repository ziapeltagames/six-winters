# -*- coding: utf-8 -*-
"""
Script to approximate game length. Players have some control over drawing
encounter cards, depending on season.    
"""

import sys, statistics

from trigger_deck import TriggerDeck

def draw_card(mdeck):
    
    card = mdeck.draw()
    if card == None:
        mdeck.shuffle()
        card = mdeck.draw()
    mdeck.discard(card)
        
    return card

def draw_trigger(mdeck, trigger, player_draws, total_player_draws,
                 winter = False):
    
    match = False
    
    card = draw_card(mdeck)
        
    if winter:
        while trigger not in card.trigger and player_draws < total_player_draws:
            player_draws = player_draws + 1
            card = draw_card(mdeck)            
    else:
        while trigger in card.trigger and player_draws < total_player_draws:
            player_draws = player_draws + 1
            card = draw_card(mdeck)
        
    if trigger in card.trigger:
        match = True
        
    return match, player_draws

edeck = TriggerDeck('Empire', 'trigger-cards.csv')
rdeck = TriggerDeck('Red Bank', 'trigger-cards.csv')
sdeck = TriggerDeck('Settled Lands', 'trigger-cards.csv')

decks = [edeck, rdeck, sdeck]
stages=['xxSPRING', 'xxSPRING', 'xxSUMMER', 'xxSUMMER', 'xxFALL', 'xxFALL']

total_player_draws = [1, 1, 1, 2, 2, 2]

# Total Turns 8.981 9.0 1.8857876856091715
# Spring 3.007 3.0 1.0430910981496482
# Summer 3.781 4.0 1.4138734165539848
# Fall 2.193 2.0 0.4335192486371729

# total_player_draws = [1, 1, 2, 2, 3, 3]

# Total Turns 10.956 11.0 2.4322787628024836
# Spring 3.033 3.0 1.0319767322842004
# Summer 3.789 4.0 1.3958608195043758
# Fall 4.134 4.0 1.5173484591043502

total_stages = len(stages)

# How many times will players try to remove matching symbols on a turn?
trials = 1000
turns_l = []

spring_turns_l = []
summer_turns_l = []
fall_turns_l = []
winter_turns_l = []

for trial in range(trials):
    
    # Reset state each trial
    turns = 0
    winter_turns = 0
    fall_turns = 0
    summer_turns = 0
    spring_turns = 0
    
    stage = 0
    
    while stage < total_stages:
        
        player_draws = 0
        turns = turns + 1
        match = False
        winter = False
        
        if stages[stage] == 'xxSUMMER':
            summer_turns = summer_turns + 1
        elif stages[stage] == 'xxSPRING':
            spring_turns = spring_turns + 1
        elif stages[stage] == 'xxWINTER':
            winter = True
            winter_turns = winter_turns + 1 
        elif stages[stage] == 'xxFALL':
            fall_turns = fall_turns + 1
        
        season_cards = []
        
        season_match = False
        
        # Draw one card from each deck
        for next_deck in decks:
            
            match, player_draws = draw_trigger(next_deck, stages[stage], 
                                               player_draws, total_player_draws[stage],
                                               winter)
            if match == True:
                season_match = True
        
        if season_match == True:
            stage = stage + 1
    
    spring_turns_l.append(spring_turns)
    summer_turns_l.append(summer_turns)
    winter_turns_l.append(winter_turns)
    fall_turns_l.append(fall_turns)
    turns_l.append(turns)

print('Total Turns', statistics.mean(turns_l), statistics.median(turns_l), 
      statistics.stdev(turns_l))
print('Spring', statistics.mean(spring_turns_l), statistics.median(spring_turns_l), 
      statistics.stdev(spring_turns_l))
print('Summer', statistics.mean(summer_turns_l), statistics.median(summer_turns_l), 
      statistics.stdev(summer_turns_l))
print('Fall', statistics.mean(fall_turns_l), statistics.median(fall_turns_l), 
      statistics.stdev(fall_turns_l))
# print('Winter', statistics.mean(winter_turns_l), statistics.median(winter_turns_l), 
#       statistics.stdev(winter_turns_l))





