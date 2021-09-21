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
        return True, player_draws
    else:
        return False, player_draws

edeck = MissionDeck('Empire', 'Starting', 
                    '../../csv/mission-cards-obstacles.csv',
                    '../../csv/mission-cards-scenes.csv',
                    '../../csv/mission-cards-threats.csv')

rdeck = MissionDeck('Red Bank', 'Starting', 
                    '../../csv/mission-cards-obstacles.csv',
                    '../../csv/mission-cards-scenes.csv',
                    '../../csv/mission-cards-threats.csv')

sdeck = MissionDeck('Settled Lands', 'Starting', 
                    '../../csv/mission-cards-obstacles.csv',
                    '../../csv/mission-cards-scenes.csv',
                    '../../csv/mission-cards-threats.csv')

decks = [edeck, rdeck, sdeck]
stages=['xxMAIDEN', 'xxMOTHER', 'xxCRONE']
total_stages = len(stages)

# How many times will players try to remove matching symbols on a turn?
total_player_draws = 3

trials = 20000
turn_list = []
for trial in range(trials):
    
    
    # Reset state each trial
    turns = 0
    stage = 0
    for next_deck in decks:
        next_deck.shuffle()
    
    while stage < total_stages:
        
        player_draws = 0
        turns = turns + 1
        match = False
        
        # Draw one card from each deck
        for next_deck in decks:
            nmatch, player_draws = draw_trigger(next_deck, stages[stage], player_draws, total_player_draws)
            if nmatch == True:
                match = True
                
        if match == True:
            stage = stage + 1
    
    turn_list.append(turns)
    
print(statistics.mean(turn_list))
print(statistics.median(turn_list))
print(statistics.stdev(turn_list))