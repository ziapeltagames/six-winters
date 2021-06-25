# -*- coding: utf-8 -*-
"""
Dump statistics on location decks: the frequency of fronts, skills, and
rewards.

Created on Fri May 28 18:59:53 2021

@author: phill
"""

import os, csv

import numpy as np

def populate_dicts():
    
    loc_by_year = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    loc_by_region = {"Empire": [], "Red Bank": [], "Faction": []}
    
    loc_file_name = os.path.join("..", "..", "csv", "location-cards.csv")
    
    loc_file = open(loc_file_name, newline='')
    
    loc_reader = csv.DictReader(loc_file, delimiter=',')
    
    for loc in loc_reader:
        
        year_string = loc['years']
        year_list = [int(x) for x in list(year_string)]
    
        loc['years'] = year_list
        
        for year in year_list:
            loc_by_year[year].append(loc)
            
        loc_by_region[loc['region']].append(loc)
    
    loc_file.close()
    
    return loc_by_year, loc_by_region

def md_print_dict(nd, loc_file):
    
    loc_file.write('\n')
    
    key_list = list(nd.keys())
    value_array = np.array(list(nd.values()))
    sorted_indices = np.argsort(-value_array)
    
    for i in sorted_indices:
        
        key = key_list[i]
        value = value_array[i]
        
        if type(key) is int:
            pk = key
        else:
            pk = key.replace('xx', '')
            
        loc_file.write('* '+str(pk)+': '+str(value)+'\n') #nd[key])+'\n')
    
    
def stats_by_region(loc_by_year, loc_by_region):
    
    loc_file = open(os.path.join("..", "..", "docs", "design", "LOCATION_SUMMARY.md"), 'w')
    
    total_fronts = {}
    total_skills = {}
    total_years = {}
    total_achievements = {}
    
    loc_file.write('# Location Analysis\n')
    
    for region in loc_by_region.keys():
        
        # print(region)
        fronts, skills, years, achievements = front_and_skills_by_year(loc_by_region[region])
        
        loc_file.write(str('\n## '+region+' Locations by Front\n'))
        # print(fronts)
        md_print_dict(fronts, loc_file)
        
        loc_file.write(str('\n## '+region+' Locations by Skill\n'))
        # print(skills)
        md_print_dict(skills, loc_file)
        
        loc_file.write(str('\n## '+region+' Locations by Achievement\n'))
        # print(achievements)
        md_print_dict(achievements, loc_file)
        
        loc_file.write(str('\n## '+region+' Locations by Year\n'))
        # print(years)
        md_print_dict(years, loc_file)
        
        for front in fronts:
            
            if front in total_fronts:
                total_fronts[front] += fronts[front]
            else:
                total_fronts[front] = fronts[front]

        for skill in skills:
            
            if skill in total_skills:
                total_skills[skill] += skills[skill]
            else:
                total_skills[skill] = skills[skill]   
                
        for year in years:
            
            if year in total_years:
                total_years[year] += years[year]
            else:
                total_years[year] = years[year]
                
        for achievement in achievements:
            
            if achievement in total_achievements:
                total_achievements[achievement] += achievements[achievement]
            else:
                total_achievements[achievement] = achievements[achievement]
                
    loc_file.write('\n## Total Locations by Front\n')
    md_print_dict(total_fronts, loc_file)
    
    loc_file.write('\n## Total Locations by Skill\n')
    md_print_dict(total_skills, loc_file)
    
    loc_file.write('\n## Total Locations by Achievement\n')
    md_print_dict(total_achievements, loc_file)
    
    loc_file.write('\n## Total Locations by Year\n')
    md_print_dict(total_years, loc_file)
    
    loc_file.close()
            

def front_and_skills_by_year(loc_by_region):

    fronts = {}
    skills = {}
    achievements = {}
    years = {}

    for loc in loc_by_region:
        
        for year in loc['years']:
            
            if year in years:
                years[year] += 1
            else:
                years[year] = 1
            
            front = loc['front']
            
            if front in fronts:
                fronts[front] += 1
            else:
                fronts[front] = 1
                
            skill = loc['skill']
            
            if skill in skills:
                skills[skill] += 1
            else:
                skills[skill] = 1     
                
            ach = loc['achievements']
            
            if ach in achievements:
                achievements[ach] += 1
            else:
                achievements[ach] = 1                  
            
    return fronts, skills, years, achievements

loc_by_year, loc_by_region = populate_dicts()
stats_by_region(loc_by_year, loc_by_region)