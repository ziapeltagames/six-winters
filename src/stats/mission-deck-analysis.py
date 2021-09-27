# -*- coding: utf-8 -*-
"""
Dump statistics on location decks: the frequency of fronts, skills, and
rewards.

Created on Fri May 28 18:59:53 2021

@author: phill
"""

import os, csv
import numpy as np
from collections import Counter

def populate_dicts():
    
    skill_by_region = {"Empire": [], "Red Bank": [], "Settled Lands": []}
    threat_by_region = {"Empire": [], "Red Bank": [], "Settled Lands": []}
    
    mission_file_name = os.path.join("..", "..", "csv", "mission-cards.csv")
    mission_file = open(mission_file_name, newline='')
    mission_reader = csv.DictReader(mission_file, delimiter=',')
    
    for mc in mission_reader:
        
        threats = mc['threats']
        skill = mc['skill']
        region = mc['region']
        
        skill = skill.replace('xx', '')
        skill_by_region[region].append(skill)
        
        if threats != "":
            threats = threats.replace('##NBSP##', '')
            threats = threats.replace('xx', '')
            threat_by_region[region].append(threats)
    
    mission_file.close()
    
    return skill_by_region, threat_by_region

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
    
skill_by_region, threat_by_region = populate_dicts()
tally_dict('Skills', skill_by_region)
print('')
tally_dict('Threats', threat_by_region)