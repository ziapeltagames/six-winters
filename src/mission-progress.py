# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 19:33:01 2018

@author: zia
"""

from random import shuffle
import statistics

# 22 card timer deck seems good for a 16 card encounter deck
# 0.8 - 1.2 apoth
# 8 - 12 discord
# 15 - 22 cards
# 4, 5, 5, 6 = 20 cards total

epochs = 10000
deck_size = 16
sections = 3
matches = 3
draw_dict = {}

timer_deck = []

timer_deck.append('event')
timer_deck.append('event')
timer_deck.append('event')
timer_deck.append('event')
timer_deck.append('event')
timer_deck.append('event')
timer_deck.append('event')
timer_deck.append('event')
timer_deck.append('event')
timer_deck.append('event')
#timer_deck.append('event')
#timer_deck.append('event')
#timer_deck.append('event')
#timer_deck.append('event')

#About one more than number of tags
timer_deck.append('gang, oned')
timer_deck.append('gang, oned')
timer_deck.append('gang, apoth')
timer_deck.append('gang, oned')
timer_deck.append('forceful, oned')
timer_deck.append('forceful, threat')
timer_deck.append('forceful, oned')
timer_deck.append('quick, twod')
timer_deck.append('weird, threed')
timer_deck.append('sneaky, twod')

for i in range(sections):
    draw_dict[i] = []
    
gang_list = []
discord_list = []

for e in range(epochs):

    discord = 0
    gang = 0
    draws = 0
    for i in range(sections):
        
        events = 0
        shuffle(timer_deck)
        
        for card in timer_deck:
            draws = draws + 1
            if 'event' in card:
                events = events + 1
            if 'oned' in card:
                discord = discord + 1
            if 'twod' in card:
                discord = discord + 2
            if 'threed' in card:
                discord = discord + 3
            if 'quick' in card:
                gang = gang + 1
            if draws == deck_size:
                break
            if events == matches:
                break
            
        for j in range(matches):
            timer_deck.remove('event')
            
        draw_dict[i].append(draws)
        
    gang_list.append(gang)
    discord_list.append(discord)
    
    for i in range(sections):
        for j in range(matches):
            timer_deck.append('event')
    
prev_avg = 0

print('Apoth: ',sum(gang_list) / len(gang_list))
print('Discord: ',sum(discord_list) / len(discord_list))

for i in range(sections):
    cur_avg = sum(draw_dict[i]) / len(draw_dict[i])
    print(i,' avg: ',cur_avg,' diff: ',cur_avg - prev_avg,' stdev: ',statistics.stdev(draw_dict[i]))
    prev_avg = cur_avg
    
#    print(i,' median: ',statistics.median(draw_dict[i]))
#    print(i,' stdev: ',statistics.stdev(draw_dict[i]))