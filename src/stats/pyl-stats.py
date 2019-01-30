# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 19:33:01 2018

@author: zia
"""

from random import shuffle
import statistics

def remove_bysubs(rlist, rsubstring):

    rindex = 0
    for next_string in rlist:
        if rsubstring in next_string:
            break
        rindex = rindex + 1
    rlist.pop(rindex)
    return rlist
    
def build_deck():
    timer_deck = []
    timer_deck.append('TIMER,DARKNESS,ELDRITCH')
    timer_deck.append('TIMER,TRAP,ELDRITCH')
    timer_deck.append('TIMER,SAFE,ELDRITCH')
    timer_deck.append('TIMER,MISFORTUNE,ELDRITCH')
    timer_deck.append('TIMER,MISFORTUNE,ELDRITCH')
    timer_deck.append('TIMER,SAFE,ELDRITCH')
    timer_deck.append('TIMER,MISFORTUNE,ELDRITCH')
    timer_deck.append('TIMER,SAFE,ELDRITCH')
    timer_deck.append('TIMER,MISFORTUNE,ELDRITCH')
    timer_deck.append('TIMER,TRAP,ELDRITCH')
    
    timer_deck.append('DISCORD,DOOM,SNEAKY')
    timer_deck.append('PROGRESS,SORCERY,SNEAKY')
    timer_deck.append('DISCORD,DARKNESS,SNEAKY')
    timer_deck.append('PROGRESS,DARKNESS,SNEAKY')
    timer_deck.append('PROGRESS,TRAP,SNEAKY')
    timer_deck.append('DISCORD,DARKNESS,SNEAKY')
    timer_deck.append('PROGRESS,DOOM,SNEAKY')
    timer_deck.append('PROGRESS,DISASTER,SNEAKY')
    timer_deck.append('DISCORD,DOOM,SNEAKY')
    timer_deck.append('APOTHEOSIS,DOOM,SNEAKY')
    return timer_deck
    
epochs = 100000
deck_size = len(build_deck())
sections = 3
matches_list = [2,3]
current_trigger = 'ELDRITCH'
turns_dict = {}

for matches in matches_list:
    
    for i in range(sections):
        turns_dict[i] = []
        
    discord_list = []
    
    for e in range(epochs):
    
        timer_deck = build_deck()
        discord = 0
        turns = 0
        for i in range(sections):
            
            timer = 0
            shuffle(timer_deck)
            
            for card in timer_deck:
                turns = turns + 1
                if 'TIMER' in card:
                    timer = timer + 1 
                if current_trigger in card:
                    discord = discord + 1
                if timer == matches:
                    break
                
            for j in range(matches):
                timer_deck = remove_bysubs(timer_deck,'TIMER')
                
            turns_dict[i].append(turns)
            
        discord_list.append(discord)
        
    prev_avg = 0
    
    print('Timer Matches: ',matches)
#    print(current_trigger ,sum(discord_list) / len(discord_list))
    
    for i in range(sections):
        cur_avg = sum(turns_dict[i]) / len(turns_dict[i])
#        print('stage: ',i,' turns: ',cur_avg,' diff: ',cur_avg - prev_avg,' stdev: ',statistics.stdev(turns_dict[i]))
        print('stage: ',i,' turns: ',cur_avg,' stdev: ',statistics.stdev(turns_dict[i]))
        prev_avg = cur_avg
        
    #    print(i,' median: ',statistics.median(draw_dict[i]))
    #    print(i,' stdev: ',statistics.stdev(draw_dict[i]))