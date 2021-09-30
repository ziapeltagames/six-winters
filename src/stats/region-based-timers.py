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

Experiment 4: Every timer counts. [1, 2, 2, 1]

Total Turns 9.1118 9.0 2.7681823145640774
    
"""

import sys, statistics

sys.path.append('../ui')

from mission_deck import MissionDeck

def draw_trigger(mdeck):
    
    card = mdeck.draw()
    
    if card == None:
        mdeck.shuffle()
        card = mdeck.draw()
    
    mdeck.discard(card)
    
    return card.trigger

# Create three decks

edeck = MissionDeck('Empire', 'Starting', 
                    '../../csv/mission-cards.csv')

rdeck = MissionDeck('Red Bank', 'Starting', 
                    '../../csv/mission-cards.csv')

sdeck = MissionDeck('Settled Lands', 'Starting', 
                    '../../csv/mission-cards.csv')

decks = [edeck, rdeck, sdeck]
stages=['xxSPRING', 'xxSUMMER', 'xxFALL'] #, 'xxWINTER']

total_stages = len(stages)

trials = 5000
turn_list = []

for trial in range(trials):
    
    # Reset state each trial
    turns = 0
    rstages = [0, 0, 0]
    
    for next_deck in decks:
        next_deck.shuffle()
    
    while rstages[0] < total_stages and rstages[1] < total_stages and rstages[2] < total_stages:
        
        player_draws = 0
        turns = turns + 1
        
        # Draw one card from each deck
        for next_deck, next_counter in zip(decks, rcounters):
            ctrigger = draw_trigger(next_deck)

            if ctrigger == stages[next_counter]:
                next_counter = next_counter + 1

        if season_matches >= stage_lengths[stage]:
            stage = stage + 1
            season_matches = 0
    
    turn_list.append(turns)
    

# print('Total Turns', statistics.mean(turn_list), statistics.median(turn_list), statistics.stdev(turn_list))





