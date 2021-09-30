# -*- coding: utf-8 -*-
"""
If any discarded timer moves the season forward:
    
[1, 2, 2, 1]
Total Turns 9.0388 9.0 2.713736802544915   
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
stages=['xxSPRING', 'xxSUMMER', 'xxFALL']
stage_lengths=[1, 3, 2]

total_stages = len(stages)

trials = 5000
turn_list = []
sp_turns = []
su_turns = []
fa_turns = []
wi_turns = []

for trial in range(trials):
    
    # Reset state each trial
    turns = 0
    stage = 0
    season_matches = 0
    season_turns = 0
    
    for next_deck in decks:
        next_deck.shuffle()
    
    while stage < total_stages:
        
        player_draws = 0
        turns = turns + 1
        season_turns = season_turns + 1
        
        # Draw one card from each deck
        for next_deck in decks:
            ctrigger = draw_trigger(next_deck)

            if ctrigger == stages[stage]:
                season_matches = season_matches + 1

        if season_matches >= stage_lengths[stage]:
            
            if stage == 0:
                sp_turns.append(season_turns)
            elif stage == 1:
                su_turns.append(season_turns)
            elif stage == 2:
                fa_turns.append(season_turns)
            else:
                wi_turns.append(season_turns)

            stage = stage + 1
            season_matches = 0
            season_turns = 0
            
    
    turn_list.append(turns)
    

print(stage_lengths)
print('Total Turns', statistics.mean(turn_list), statistics.median(turn_list), statistics.stdev(turn_list))
print('Season Turns', statistics.mean(sp_turns), statistics.mean(su_turns), statistics.mean(fa_turns))
print('Season Stdevs', statistics.stdev(sp_turns), statistics.stdev(su_turns), statistics.stdev(fa_turns))





