# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 04:28:35 2019

@author: zia
"""

from random import shuffle
from tqdm import tqdm
import statistics
import numpy as np

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
    timer_deck.append(lambda x: 0)
    timer_deck.append(lambda x: x - 2)
    timer_deck.append(lambda x: x - 2)
    timer_deck.append(lambda x: x - 1)
    timer_deck.append(lambda x: x - 1)    
    timer_deck.append(lambda x: x)
    timer_deck.append(lambda x: x)
    timer_deck.append(lambda x: x)
    timer_deck.append(lambda x: x + 1)    
    timer_deck.append(lambda x: x + 1)
    timer_deck.append(lambda x: x + 2)
    timer_deck.append(lambda x: 2 * x)
    
    timer_deck.append(lambda x: 0)
    timer_deck.append(lambda x: x - 2)
    timer_deck.append(lambda x: x - 2)
    timer_deck.append(lambda x: x - 1)
    timer_deck.append(lambda x: x - 1)    
    timer_deck.append(lambda x: x)
    timer_deck.append(lambda x: x)
    timer_deck.append(lambda x: x)
    timer_deck.append(lambda x: x + 1)    
    timer_deck.append(lambda x: x + 1)
    timer_deck.append(lambda x: x + 2)
    timer_deck.append(lambda x: 2 * x)
    return timer_deck
    
epochs = 100000
deck_size = len(build_deck())
single_vals = [3, 3]
group_val = np.sum(single_vals)

single_draw = []
    
for e in tqdm(range(epochs)):

    timer_deck = build_deck()
    shuffle(timer_deck)
    single_draw.append(timer_deck[0](group_val))
    
single_avg = sum(single_draw) / len(single_draw)
print('Single ',single_avg,' ')
print('STD ',statistics.stdev(single_draw[:10000]))

double_draw = []
    
for e in tqdm(range(epochs)):

    timer_deck = build_deck()
    shuffle(timer_deck)
    double_draw.append(timer_deck[0](single_vals[0]) + timer_deck[1](single_vals[1]))
    
double_avg = sum(double_draw) / len(double_draw)
print('Double ',double_avg,' ')
print('STD ',statistics.stdev(double_draw[:10000]))

print('Difference ',single_avg - double_avg)