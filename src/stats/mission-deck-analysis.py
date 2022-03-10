# -*- coding: utf-8 -*-
"""
Dump statistics on mission deck. Histograms for all of the categories.

Created on Fri May 28 18:59:53 2021

@author: phill
"""

import os, csv
from collections import Counter


def tally(dict_ref, value):

    if value in dict_ref.keys():
        dict_ref[value] = dict_ref[value] + 1
    else:
        dict_ref[value] = 1


def tally_tag(dict_ref, values):

    values = values.replace('##NBSP##', '')
    values = values.replace('xx', ' ')
    values = values[1:]
    values = values.split(' ')
        
    for value in values:
        if value == '':
            continue
        tally(dict_ref, value)

        
def tally_defense_dice(dict_ref, dice_text):
    
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for num in nums:
        dice_text = dice_text.replace(num, '')
    tally_dice(dict_ref, dice_text)
    
def tally_dice(dict_ref, dice_text):
    
    dice_text = dice_text.replace('##NBSP##', '')
    dice_text = dice_text.replace(' xxOVERCOME', '')
    dice_text = dice_text.replace(' xxFIRE', '')
    dice_text = dice_text.replace('xxBODY', '')
    dice_text = dice_text.replace('xxPSYCHE', '')
    dice_text = dice_text.replace('FLAKE', '')
    dice = dice_text.split('xx')
    for die in dice:
        if die=='':
            continue
        die = die.replace(' ', '')
        tally(dict_ref, die)


def populate_dicts():
    
    total_threats = {}
    threats_by_region = {"EMPIRE": {}, "REDBANK": {}, "SETTLED": {}}
    
    total_skills = {}
    skills_by_region = {"EMPIRE": {}, "REDBANK": {}, "SETTLED": {}}
    
    total_defense = {}
    total_offense = {}
    
    mission_file_name = os.path.join("..", "..", "csv", "mission-cards.csv")
    mission_file = open(mission_file_name, newline='')
    mission_reader = csv.DictReader(mission_file, delimiter=',')
    
    for mc in mission_reader:

        region = mc['region']
        region = region.replace('xx', '')
        
        threats = mc['threats']
        tally_tag(threats_by_region[region], threats)
        tally_tag(total_threats, threats)
        
        skill = mc['skill']
        tally_tag(skills_by_region[region], skill)
        tally_tag(total_skills, skill)
        
        def1 = mc['defense1']
        tally_dice(total_defense, def1)
        def2 = mc['defense2']
        tally_dice(total_defense, def2)
        
        att1 = mc['attack1']
        tally_defense_dice(total_offense, att1)
        att2 = mc['attack2']
        tally_defense_dice(total_offense, att2)
    
    mission_file.close()
    
    print('THREATS', '\n')
    # print(threats_by_region, '\n')
    print(total_threats, '\n')
    
    print('SKILLS', '\n')
    # print(skills_by_region, '\n')
    print(total_skills, '\n')
    
    print('OVERCOME', '\n')
    print(total_defense, '\n')
    
    print('DAMAGE', '\n')
    print(total_offense, '\n')
    

def tally_dict(dict_name, sw_dict):
    
    print(dict_name)
    
    ec = Counter(sw_dict['Empire'])
    rbc = Counter(sw_dict['Red Bank'])
    sbc = Counter(sw_dict['Settled Lands'])

    print('Empire', ec)
    print('Red Bank', rbc)
    print('Settled Lands', sbc)
    
    total_dict = {}
    for ds in [ec, rbc, sbc]:
        for ni in ds.items():
            nkey, nval = ni[0], ni[1]
        
            if nkey in total_dict:
                total_dict[nkey] = total_dict[nkey] + nval
            else:
                total_dict[nkey] = nval
                
    print('Total', total_dict)
    
populate_dicts()