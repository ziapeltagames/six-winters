# -*- coding: utf-8 -*-
"""
Simple class to manage drawing progress deck and mission cards.

Created on Tue Feb 13 21:26:54 2018

@author: zia
"""

from random import shuffle

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
                 "shuffle,,,"]

p1 = list(progress_deck)
p2 = list(progress_deck)
shuffle(p1)
shuffle(p2)
p1ind = 0
p2ind = 0

northoaks_deck = ['Hand Resource Food Source Action: +3 Food. Roll dice and add to pool. Season End: +1 Food track. Burn card',
                  'Hand Resource Timber Source Action: +3 Timber. Roll dice and add to pool. Season End: +1 Timber track. Burn card',
                  'Hand Resource Timber Source Action: +3 Timber. Roll dice and add to pool. Season End: +1 Timber track. Burn card',
                  'Hand Resource Ore Source Action: +3 Ore. Roll dice and add to pool. Season End: +1 Ore track. Burn card',
                  'Hand Resource Mana Source Action: +3 Mana. Roll dice and add to pool. Season End: +1 Mana track. Burn card',
                  'Event Foe Poisonous Dusk Frogs Solo Combat: 1. Success: +1 Combat. Burn card. Failure: Wounded',
                  'Event Obstacle Rocky Terrain Survival: 2. Failure: All characters are weary',
                  'Event Magic Libram of Animation Solo Lore: 1. Success: +1 Lore. Burn card. Failure: Weary',
                  'Attachment Wilderness Clearing the Woods Placement: Mirror Woods Optional Test: Survival 2. Success: +1 Timber',
                  'Attachment Foe Animated Dead Placement: Any occupied location in North Oaks. Optional Ongoing Test: Combat. Progress 4. Completion: Discard. Strong: Combat Test: 3.  North Oaks location with lowest Lore character',
                  'Attachment Wilderness Trackless Forest Placement: Any wilderness location. Effect: While any character at attached location, may use timber resource dice as skill test',
                  'Attachment Environment Grueling Wilds Placement: On character with lowest survival. Quick: Solo Test: Survival 2. Failure: Weary. On Movement: If character moves out of wilderness location, remove condition']

m1 = list(northoaks_deck)
m2 = list(northoaks_deck)
shuffle(m1)
shuffle(m2)
m1ind = 0
m2ind = 0

while True:
    choice = input("> ")
    choice = choice.lower()
    
    if choice == 'e':
        break
    
    if choice == 'a':
        print(p1[p1ind])
        if p1[p1ind] == 'shuffle':
            shuffle(p1)
            p1ind = 0
        else:
            p1ind = p1ind+1
    
    if choice == 'b':
        print(p2[p2ind])
        if p2[p2ind] == 'shuffle':
            shuffle(p2)
            p2ind = 0
        else:
            p2ind = p2ind+1

    if choice == '1':
        if m1ind < len(m1):
            print(m1[m1ind])
            m1ind = m1ind+1
        else:
            print("empty")
    
    if choice == '2':
        if m2ind < len(m2):
            print(m2[m2ind])
            m2ind = m2ind+1
        else:
            print("empty")