# -*- coding: utf-8 -*-
"""
Dump statistics on mission deck. Histograms for all of the categories.

Created on Fri May 28 18:59:53 2021

@author: phill
"""

import os, csv

cells = ["g11","g12","g13","g14","g21","g22","g23","g24","g31","g32","g33","g34","g41","g42","g43","g44","f11","f12","f13","f14","f21","f22","f23","f24","f31","f32","f33","f34","f41","f42","f43","f44"]

locations = ['EMPIRE', 'REDBANK', 'SETTLED']

dice = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX']

resources = {"Technology": ['OT', 'OS', 'OE', 'OO'], 
             #"Wild": ['WT', 'WS', 'WE', 'WW'],
             "Espionage": ['MT', 'MS', 'ME', 'MM'], 
             "Support": ['YT', 'YS', 'YE', 'YY'],
             "Military": ['GT', 'GS', 'GE', 'GG'], 
             "Sorcery": ['BT', 'BS', 'BE', 'BB'], 
             "Diplomacy": ['LT', 'LS', 'LE', 'LL']}

def tally(dict_ref, value):

    if value in dict_ref.keys():
        dict_ref[value] = dict_ref[value] + 1
    else:
        dict_ref[value] = 1
        
def tally_cell(dict_ref, value):

    values = []
    
    for loc in locations:
        if loc in value:
            values.append(loc)
        
    for die in dice:
        if die in value:
            values.append(die)
        
    for resource in resources.keys():
        for color in resources[resource]:
            if color in value[0:2]:
                values.append(resource)
        
    for nv in values:
        if nv in dict_ref.keys():
            dict_ref[nv] = dict_ref[nv] + 1
        else:
            dict_ref[nv] = 1

def populate_dicts():
    
    achievements_by_stage = {"1": {}, "2": {}, "3": {}, "4": {}}

    locations_by_stage = {"1": {}, "2": {}, "3": {}, "4": {}}
    
    mission_file_name = os.path.join("..", "..", "csv", "achievement-cards.csv")
    mission_file = open(mission_file_name, newline='')
    mission_reader = csv.DictReader(mission_file, delimiter=',')
    
    for mc in mission_reader:
        
        stage = mc['stage']
        
        for cell in cells:
            tally_cell(achievements_by_stage[stage], mc[cell])
            
        location = mc['locregion']
        location = location.replace('xx', ' ')
        location = location.replace(' ', '')
        tally(locations_by_stage[stage], location)
        
            
    for stage in achievements_by_stage.keys():
        print('\nStage', stage, 'Achievements\n')
        
        for loc in locations:
            print(loc, achievements_by_stage[stage][loc])
            
        for resource in resources.keys():
            print(resource, achievements_by_stage[stage][resource])
            
        for die in dice:
            print(die, achievements_by_stage[stage][die])
            
    for stage in locations_by_stage.keys():
        
        print('\nStage', stage, 'Locations\n')

        print('Empire Military: ', locations_by_stage[stage]['EMPIREMILITARY'])
        print('Empire Technology: ', locations_by_stage[stage]['EMPIRETECHNOLOGY'])
        print('Empire Espionage: ', locations_by_stage[stage]['EMPIREESPIONAGE'])
        print('\nRed Bank Military: ', locations_by_stage[stage]['REDBANKMILITARY'])
        print('Red Bank Stability: ', locations_by_stage[stage]['REDBANKSTABILITY'])
        print('Red Bank Sorcery: ', locations_by_stage[stage]['REDBANKSORCERY'])
        print('\nSettled Diplomacy: ', locations_by_stage[stage]['SETTLEDDIPLOMACY'])
        print('Settled Technology: ', locations_by_stage[stage]['SETTLEDTECHNOLOGY'])
        print('Settled Sorcery: ', locations_by_stage[stage]['SETTLEDSORCERY'])
    
populate_dicts()