# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 07:22:26 2018

@author: zia
"""

from random import shuffle
import statistics

progress_deck = ["timer,weather,team,common",
                 ",safe,team,rare",
                 ",suspicious,team,uncommon",
                 ",darkness,team,uncommon",
                 ",sorcery,team,common",
                 ",doom,team,common",
                 "timer,darkness,forceful,uncommon",
                 ",weather,forceful,common",
                 ",safe,forceful,common",
                 ",darkness,forceful,common",
                 ",doom,forceful,common",
                 "timer,sorcery,quick,common",
                 ",darkness,quick,uncommon",
                 ",valor,quick,common",
                 ",trap,quick,common",
                 "timer,doom,sneaky,common",
                 ",darkness,sneaky,uncommon",
                 ",safe,sneaky,common",
                 "timer,doom,weird,common",
                 ",suspicious,weird,uncommon",
                 ",doom,overwhelming,common",
                 ",trap,deadly,rare",
                 ",calamity,poisonous,common",
                 "timer,suspicious,special,uncommon",
                 "timer,blah,blah,blah",
                 "timer,blah,blah,blah",
                 "shuffle,,,"]

prd = list(progress_deck)
avg_cards = []

for i in range(0,100000):
    
    shuffle(prd)
    prd_ind = 0
    cards = 0
    timers = 0
    
    while timers <= 5:
    
        if prd[prd_ind].find('timer') >= 0:
            timers = timers + 1
        
        if prd[prd_ind].find('shuffle') >= 0:
            shuffle(prd)
            prd_ind = 0
        else:
            cards = cards + 1
            prd_ind = prd_ind+1
            
    avg_cards.append(cards)

print(statistics.median(avg_cards))
print(len(avg_cards))
print(sum(avg_cards)/len(avg_cards))