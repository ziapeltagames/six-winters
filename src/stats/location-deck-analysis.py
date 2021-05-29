# -*- coding: utf-8 -*-
"""
Dump statistics on location decks: the frequency of fronts, skills, and
rewards.

Created on Fri May 28 18:59:53 2021

@author: phill
"""

import os, csv

def populate_dicts():
    
    loc_by_year = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    loc_by_region = {"Empire": [], "Red Bank": [], "Faction": []}
    
    loc_file_name = os.path.join("..", "..", "csv", "locations.csv")
    
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

def md_print_dict(nd):
    
    print('')
    
    for key in nd.keys():
        
        if type(key) is int:
            pk = key
        else:
            pk = key.replace('xx', '')
            
        print('* ', pk, ':', nd[key])
    
    
def stats_by_region(loc_by_year, loc_by_region):
    
    total_fronts = {}
    total_skills = {}
    total_years = {}
    total_achievements = {}
    
    for region in loc_by_region.keys():
        
        fronts, skills, years, achievements = front_and_skills_by_year(loc_by_region[region])
        
        print('## ', region, 'Locations by Front')
        md_print_dict(fronts)
        
        print('')
        print('## ', region, 'Locations by Skill')
        md_print_dict(skills)
        
        print('')
        print('## ', region, 'Locations by Achievement')
        md_print_dict(achievements)
        
        print('')
        print('## ', region, 'Locations by Year')
        md_print_dict(years)
        print('\n')
        
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
                
    print('## Total Locations by Front')
    md_print_dict(total_fronts)
    
    print('')
    print('## Total Locations by Skill')
    md_print_dict(total_skills)
    
    print('')
    print('## Total Locations by Achievement')
    md_print_dict(total_achievements)
    
    print('')
    print('## Total Locations by Year')
    md_print_dict(total_years)
            

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
                
            ach = loc['achievement']
            
            if ach in achievements:
                achievements[ach] += 1
            else:
                achievements[ach] = 1                  
            
    return fronts, skills, years, achievements
    
print('# Location Analysis \n')

loc_by_year, loc_by_region = populate_dicts()
stats_by_region(loc_by_year, loc_by_region)