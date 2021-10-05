# -*- coding: utf-8 -*-
"""
Script to approximate game length. Players have some control over drawing
encounter cards, depending on season.    
"""

import sys, statistics

from trigger_deck import TriggerDeck

def draw_trigger(mdeck, trigger, player_draws, total_player_draws,
                 winter = False):
    
    match = False
    
    card = mdeck.draw()
    
    if card == None:
        match = True
        mdeck.shuffle()
        card = mdeck.draw()
    
    mdeck.discard(card)
        
    if winter:
        
        while trigger not in card.trigger and player_draws < total_player_draws:
            
            player_draws = player_draws + 1
            card = mdeck.draw()
            if card == None:
                match = True
                mdeck.shuffle()
                card = mdeck.draw()
            mdeck.discard(card)
            
    else:
        
        while trigger in card.trigger and player_draws < total_player_draws:
            
            player_draws = player_draws + 1
            card = mdeck.draw()
            if card == None:
                match = True
                mdeck.shuffle()
                card = mdeck.draw()    
            mdeck.discard(card)
        
    if trigger in card.trigger:
        match = True
        
    return match, player_draws

edeck = TriggerDeck('Empire', 'trigger-cards.csv')

rdeck = TriggerDeck('Red Bank', 'trigger-cards.csv')

sdeck = TriggerDeck('Settled Lands', 'trigger-cards.csv')


decks = [edeck, rdeck, sdeck]
stages=['xxSPRING', 'xxSUMMER', 'xxSUMMER', 'xxFALL', 'xxFALL', 'xxWINTER']

print('Player Control')
total_player_draws = [0, 1, 1, 2, 2, 3]

#print('No Player Control')
#total_player_draws = [0, 0, 0, 0, 0, 0]

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
    
    for next_deck in decks:
        next_deck.shuffle()
    
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
        
        # Draw one card from each deck
        for next_deck in decks:
            
            match, player_draws = draw_trigger(next_deck, stages[stage], 
                                               player_draws, total_player_draws[stage],
                                               winter)
        
        if match == True:
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
print('Winter', statistics.mean(winter_turns_l), statistics.median(winter_turns_l), 
      statistics.stdev(winter_turns_l))





