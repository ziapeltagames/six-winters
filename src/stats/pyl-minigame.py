# -*- coding: utf-8 -*-
"""
A sample timer deck app for prototyping the mission based push your luck game.

Created on Tue Aug 28 23:33:30 2018

@author: zia
"""

import random
from random import shuffle

def remove_bysubs(rlist, rsubstring):

    rindex = 0
    for next_string in rlist:
        if rsubstring in next_string:
            break
        rindex = rindex + 1
    print('Found at index ',rindex,': ',rlist[rindex])
    rlist.pop(rindex)
    print('Removing ',rsubstring,' Deck size: ',len(rlist))
    return rlist

def calculate_discord(rstring):
    if '+1 DISCORD' in rstring:
        return 1
    if '+2 DISCORD' in rstring:
        return 2
    if '+3 DISCORD' in rstring:
        return 3
    if '+4 DISCORD' in rstring:
        return 4
    return 0

# Can leverage the fact that event frequency will evolve over the course
# of the game - for example, forceful things will tire themselves out
def build_four_stage_deck():
    fs_deck = []
    fs_deck.append('TIMER,CALAMITY,GANG')
    fs_deck.append('TIMER,TRAP,OVERWHELMING')
    fs_deck.append('TIMER,DOOM,DEADLY')
    fs_deck.append('TIMER,DARKNESS,POISONOUS')
    fs_deck.append('TIMER,TRAP,ELDRITCH')
    fs_deck.append('TIMER,SORCERY,FORCEFUL')
    fs_deck.append('TIMER,SAFE,QUICK')
    fs_deck.append('TIMER,SORCERY,WEIRD')
    fs_deck.append('TIMER,DARKNESS,SNEAKY')
    fs_deck.append('TIMER,TRAP,GANG')
    fs_deck.append('TIMER,MISFORTUNE,DEADLY')
    fs_deck.append('TIMER,DOOM,POISONOUS')
    fs_deck.append('TIMER,SAFE,FORCEFUL')
    fs_deck.append('TIMER,MISFORTUNE,QUICK')
    fs_deck.append('+1 DISCORD,DOOM,GANG')
    fs_deck.append('+1 DISCORD,SAFE,GANG')
    fs_deck.append('+1 APOTHEOSIS,DOOM,GANG')
    fs_deck.append('+2 DISCORD,DARKNESS,FORCEFUL')
    fs_deck.append('+1 DISCORD,MISFORTUNE,FORCEFUL')
    fs_deck.append('+2 DISCORD,DARKNESS,QUICK')
    fs_deck.append('+3 DISCORD,MISFORTUNE,WEIRD')
    fs_deck.append('+1 THREAT,MISFORTUNE,SNEAKY')
    return fs_deck

def build_three_stage_deck():
    ts_deck = []
    ts_deck.append('TIMER,DARKNESS,FORCEFUL')
    ts_deck.append('TIMER,TRAP,FORCEFUL')
    ts_deck.append('TIMER,SAFE,FORCEFUL')
    ts_deck.append('TIMER,MISFORTUNE,FORCEFUL')
    ts_deck.append('TIMER,MISFORTUNE,WEIRD')
    ts_deck.append('TIMER,SAFE,WEIRD')
    ts_deck.append('TIMER,MISFORTUNE,DEADLY')
    ts_deck.append('TIMER,SAFE,QUICK')
    ts_deck.append('TIMER,MISFORTUNE,QUICK')
    ts_deck.append('TIMER,TRAP,SNEAKY')
    ts_deck.append('+1 DISCORD,DOOM,SNEAKY')
    ts_deck.append('THREAT,SORCERY,SNEAKY')
    ts_deck.append('+2 DISCORD,DARKNESS,SNEAKY')
    ts_deck.append('+1 DISCORD,DARKNESS,QUICK')
    ts_deck.append('+1 DISCORD,TRAP,GANG')
    ts_deck.append('+1 DISCORD,DARKNESS,GANG')
    ts_deck.append('+2 DISCORD,DOOM,GANG')
    ts_deck.append('+1 DISCORD,DISASTER,GANG')
    ts_deck.append('+3 DISCORD,DOOM,POISONOUS')
    ts_deck.append('+1 APOTHEOSIS,DOOM,ELDRITCH')
    return ts_deck

timer_deck = build_three_stage_deck()
deck_index = 0

# This is the number of cards in the encounter deck
mission_length = 16

total_sections = 3
current_section = 1

timers = 0
turn = 0
discord = 0
apoth = 0
progress = 0
banked = 0
shuffle(timer_deck)

while True:
    choice = input("> ")
    choice = choice.lower() #Convert input to "lowercase"

    if choice == 'x':
        print("Bye")
        break

    if choice == 'n':
        next_card = timer_deck[deck_index]
        print(next_card)
        deck_index = deck_index + 1
        turn = turn + 1
        progress = progress + random.randint(0,6)
        discord = discord + calculate_discord(next_card)
            
        if 'APOTHEOSIS' in next_card:
            apoth = apoth + 1
            
        if 'TIMER' in next_card:
            timers = timers + 1
        
        if timers == 3:
            print('Lose progress!')
            current_section = current_section + 1
            for i in range(3):
                timer_deck = remove_bysubs(timer_deck,'TIMER')
            shuffle(timer_deck)
            deck_index = 0
            timers = 0
            progress = 0
            
    if choice == 'b':
        print("Bank progress!")
        banked = banked + progress
        progress = 0
        current_section = current_section + 1
        for i in range(timers):
            timer_deck = remove_bysubs(timer_deck,'TIMER')
        timers = 0
        deck_index = 0
        shuffle(timer_deck)

    print(turn,': Prog ',progress,' Banked ',banked,' Discord ',discord,' Apoth ',apoth,' Timers ',timers,' Section ',current_section)
            
    if current_section > total_sections:
        print('Finished All Sections!')
        break
    
    if turn == mission_length:
        print('Mission Ended!')
        banked = banked + progress
        progress = 0
        break
    
print('SCORE: ',(banked * turn) - (discord * 5) - (apoth * 20))