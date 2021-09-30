# -*- coding: utf-8 -*-
"""
How long does the average game take in the three region version?

Experiment 1: Reshuffle any deck that runs out and continue drawing. The game
ends after three stages, if any region deck matches the stage.

Pretty short! Avg of 4 turns, with a stdev of 1.

Experiment 2: Simulate players actively drawing matching trigger mission
cards. Players will draw up to two matching cards before giving up.

1 Draw: 7 turns
2 Draws: 13 turns
3 Draws: 29 turns

Experiment 3: Vary timers and lookahead.

5 Timers, 1 Lookahead: 12 turns
    
"""

import sys, statistics

sys.path.append('../ui')

from mission_deck import MissionDeck

def draw_trigger(mdeck, trigger, player_draws, total_player_draws):
    
    card = mdeck.draw()
    
    if card == None:
        mdeck.shuffle()
        card = mdeck.draw()
    
    mdeck.discard(card)
    
    while card.trigger == trigger and player_draws < total_player_draws:
        
        player_draws = player_draws + 1
        
        card = mdeck.draw()
        
        if card == None:
            mdeck.shuffle()
            card = mdeck.draw()
            
        mdeck.discard(card)
        
    if card.trigger == trigger:
        return True, player_draws, card
    else:
        return False, player_draws, card

edeck = MissionDeck('Empire', 'Starting', 
                    '../../csv/mission-cards-obstacles.csv',
                    '../../csv/mission-cards-threats.csv')

rdeck = MissionDeck('Red Bank', 'Starting', 
                    '../../csv/mission-cards-obstacles.csv',
                    '../../csv/mission-cards-threats.csv')

sdeck = MissionDeck('Settled Lands', 'Starting', 
                    '../../csv/mission-cards-obstacles.csv',
                    '../../csv/mission-cards-threats.csv')

decks = [edeck, rdeck, sdeck]
stages=['xxSPRING', 'xxSUMMER', 'xxSUMMER', 'xxFALL', 'xxFALL', 'xxWINTER']
total_stages = len(stages)

# How many times will players try to remove matching symbols on a turn?
total_player_draws = 1 # 3

trials = 1000
turn_list = []
winter_list = []
fall_list = []
sb_threat_list = []

threat_deck_list = []

for trial in range(trials):
    
    # Reset state each trial
    turns = 0
    winter_turns = 0
    fall_turns = 0
    stage = 0
    sb_threats = 0
    
    for next_deck in decks:
        next_deck.shuffle()
    
    while stage < total_stages:
        
        player_draws = 0
        turns = turns + 1
        match = False
        
        if stages[stage] == 'xxWINTER':
            winter_turns = winter_turns + 1          
            
        if stages[stage] == 'xxFALL':
            fall_turns = fall_turns + 1
        
        season_cards = []
        
        # Draw one card from each deck
        for next_deck in decks:
            nmatch, player_draws, card = draw_trigger(next_deck, stages[stage], player_draws, total_player_draws)
            if nmatch == True:
                match = True
            season_cards.append(card)
        
        if stages[stage] == 'xxSPRING' or stages[stage] == 'xxSUMMER':
            if season_cards[0].tags == 'Threat':
                sb_threats = sb_threats + 1
                
        if stages[stage] == 'xxFALL' or stages[stage] == 'xxWINTER':
            if season_cards[1].tags == 'Threat':
                sb_threats = sb_threats + 1
        
        if match == True:
            stage = stage + 1
    
    sb_threat_list.append(sb_threats)
    winter_list.append(winter_turns)
    fall_list.append(fall_turns)
    turn_list.append(turns)
    

print('Threats', statistics.mean(sb_threat_list), statistics.median(sb_threat_list), statistics.stdev(sb_threat_list))

print('Total Turns', statistics.mean(turn_list), statistics.median(turn_list), statistics.stdev(turn_list))

print('Fall', statistics.mean(fall_list), statistics.median(fall_list), statistics.stdev(fall_list))
print('Winter', statistics.mean(winter_list), statistics.median(winter_list), statistics.stdev(winter_list))





