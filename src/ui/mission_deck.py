# -*- coding: utf-8 -*-
"""
Deck of mission cards.
"""

import csv

from deck import Deck


class MissionCard:
    
    def __init__(self, cdict, category, region = None):
        
        # Threats don't have most of the usual mission card data
        if category == 'Threat':
            cdict['region'] = region
            cdict['name'] = ""
            cdict['tags'] = ""
            cdict['skill'] = ""
            cdict['difficulty'] = ""
            cdict['effect'] = ""
            cdict['activation'] = ""
            cdict['overcome'] = ""
            # cdict['bust'] = ""
        
        self.region = cdict['region'] 
        self.trigger = cdict['trigger']
        self.stage = cdict['stage']        
        self.name = cdict['name']
        self.tags = cdict['tags']
        self.skill = cdict['skill']
        self.defense = cdict['defense']
        self.difficulty = cdict['difficulty']
        self.attack = cdict['attack']
        self.effect = cdict['effect']
        self.activation = cdict['activation']
        self.overcome = cdict['overcome']
        
        self.category = category
        
    def __str__(self):
        cstring = self.category + ' ' + self.name
        return cstring
    
class MissionDeck(Deck):
    
    def __init__(self, region, stage, obstacles, scenes, 
                 threats, num_threats = 12):

        self.num_threats = num_threats
        
        mission_cards = []
        
        mission_cards.extend(self.read_deck(region, 
                                            stage, 'Obstacle', obstacles))
        mission_cards.extend(self.read_deck(region, 
                                            stage, 'Scene', scenes))
        mission_cards.extend(self.read_deck(region, 
                                            stage, 'Threat', threats))
        
        super().__init__(mission_cards)
        
    def read_deck(self, region, stage, category, csv_file):
        
        total_threats = 0
        
        mission_cards = []
        with open(csv_file) as csvfile:
            dreader = csv.DictReader(csvfile)
            for rowd in dreader:
                
                if category == 'Threat':
                    next_card = MissionCard(rowd, category, region)
                else:
                    next_card = MissionCard(rowd, category)
                
                if region not in next_card.region:
                    continue
                
                if stage not in next_card.stage:
                    continue
                
                if category == 'Threat' and total_threats >= self.num_threats:
                    continue
                
                if category == 'Threat':
                    total_threats = total_threats + 1

                mission_cards.append(next_card)

        return mission_cards
    
    def top_trigger(self):
        
        if len(self.cards) > 0:
            return self.cards[0].trigger
        else:
            return "Empty"
        
    # Draw a number of cards equal to stage, return list of triggers
    def draw_triggers(self, month):
        
        if month > 3:
            month = 3

        triggers = ["", "", ""]
    
        for i in range(month):   
            next_card = self.draw()
            
            if next_card:
                next_trigger = next_card.trigger
                triggers[i] = next_trigger
                self.discard(next_card)
                
            else:
                return None
            
        return triggers
          
if __name__ == "__main__":
    
    cdeck = MissionDeck('Empire', 'Starting', 
                        '../../csv/mission-cards-obstacles.csv',
                        '../../csv/mission-cards-scenes.csv',
                        '../../csv/mission-cards-threats.csv')
    
    cc = cdeck.draw()
    print('draw', cc)
    cdeck.discard(cc)
    
    cc = cdeck.draw()
    print('draw', cc)
    cdeck.discard(cc)
    
    cc = cdeck.draw()
    print('draw', cc)
    cdeck.discard(cc)
    
    cdeck.shuffle()
    
    cc = cdeck.draw()
    print('draw', cc)
    cdeck.discard(cc)
    
    cc = cdeck.draw()
    print('draw', cc)
    cdeck.discard(cc)
    
    cc = cdeck.draw()
    print('draw', cc)
    cdeck.discard(cc)