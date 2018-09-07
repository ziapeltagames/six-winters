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
    timer_deck.append('TIMER,DARKNESS,FORCEFUL')
    timer_deck.append('TIMER,TRAP,FORCEFUL')
    timer_deck.append('TIMER,SAFE,FORCEFUL')
    timer_deck.append('TIMER,MISFORTUNE,FORCEFUL')
    timer_deck.append('TIMER,MISFORTUNE,WEIRD')
    timer_deck.append('TIMER,SAFE,WEIRD')
    timer_deck.append('TIMER,MISFORTUNE,DEADLY')
    timer_deck.append('TIMER,SAFE,QUICK')
    timer_deck.append('TIMER,MISFORTUNE,QUICK')
    timer_deck.append('TIMER,TRAP,SNEAKY')
    
    timer_deck.append('PROGRESS,DOOM,SNEAKY')
    timer_deck.append('THREAT,SORCERY,SNEAKY')
    timer_deck.append('DISCORD,DARKNESS,SNEAKY')
    timer_deck.append('PROGRESS,DARKNESS,QUICK')
    timer_deck.append('PROGRESS,TRAP,GANG')
    timer_deck.append('DISCORD,DARKNESS,GANG')
    timer_deck.append('PROGRESS,DOOM,GANG')
    timer_deck.append('PROGRESS,DISASTER,GANG')
    timer_deck.append('DISCORD,DOOM,GANG')
    timer_deck.append('APOTHEOSIS,DOOM,ELDRITCH')
    return timer_deck

# Stats:
    
# SNEAKY 2.6 - 3.7
# QUICK 1.8 - 2.4
    
# Only on non-timer cards
# GANG 3.3 - 4.9
# ELDRITCH 0.7 - 0.9
    
# Only on timer cards
# FORCEFUL 2.3 - 2.9 (max 4)
# WEIRD 1.2 - 1.4 (max 2)
# DEADLY 0.5 - 0.7 (max 1)
    
epochs = 10000
deck_size = 16
sections = 3
matches = 3
current_trigger = 'GANG'
draw_dict = {}

for i in range(sections):
    draw_dict[i] = []
    
progress_list = []
discord_list = []

for e in range(epochs):

    timer_deck = build_deck()
    discord = 0
    progress = 0
    draws = 0
    for i in range(sections):
        
        timer = 0
        shuffle(timer_deck)
        
        for card in timer_deck:
            draws = draws + 1
            if 'TIMER' in card:
                timer = timer + 1
            if 'PROGRESS' in card:
                progress = progress + 1
            if current_trigger in card:
                discord = discord + 1
            if draws == deck_size:
                break
            if timer == matches:
                break
            
        for j in range(matches):
            timer_deck = remove_bysubs(timer_deck,'TIMER')
            
        draw_dict[i].append(draws)
        
    progress_list.append(progress)
    discord_list.append(discord)
    
prev_avg = 0

print('Progress: ',sum(progress_list) / len(progress_list))
print('Current Trigger: ',sum(discord_list) / len(discord_list))

for i in range(sections):
    cur_avg = sum(draw_dict[i]) / len(draw_dict[i])
    print(i,' avg: ',cur_avg,' diff: ',cur_avg - prev_avg,' stdev: ',statistics.stdev(draw_dict[i]))
    prev_avg = cur_avg
    
#    print(i,' median: ',statistics.median(draw_dict[i]))
#    print(i,' stdev: ',statistics.stdev(draw_dict[i]))