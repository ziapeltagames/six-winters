# -*- coding: utf-8 -*-
"""
Deck of mission cards.
"""

import csv

from deck import Deck

class MissionCard:
    
    def __init__(self, cdict, category):

        self.region = cdict['region'] 
        self.trigger = cdict['trigger']
        self.stage = cdict['stage']
        self.name = cdict['name']
        self.tags = cdict['tags']
        self.skill = cdict['skill']
        self.resource = cdict['resource']
        self.defense = cdict['defense']
        self.difficulty = cdict['difficulty']
        self.attack = cdict['attack']
        self.effect = cdict['effect']
        self.activation = cdict['activation']
        self.overcome = cdict['overcome']
        self.bust = cdict['bust']
        
        self.category = category
        
    def __str__(self):
        cstring = self.category + ' ' + self.name + ' ' + self.tags + ' ' + \
            ' ' + self.skill + ' ' + self.resource + \
            ' ' + self.defense + ' ' + self.difficulty + ' ' + self.attack + \
            ' ' + self.effect + ' ' + self.activation + ' ' + self.bust
        return cstring
    
class MissionDeck(Deck):
    
    def __init__(self, region, stage, obstacles, scenes, twists, threats):

        mission_cards = []
        
        mission_cards.extend(self.read_deck(region, 
                                            stage, 'Obstacle', obstacles))
        mission_cards.extend(self.read_deck(region, 
                                            stage, 'Scene', scenes))
        mission_cards.extend(self.read_deck(region, 
                                            stage, 'Twist', twists))
        mission_cards.extend(self.read_deck(region, 
                                            stage, 'Threat', threats))
        
        super().__init__(mission_cards)
        
    def read_deck(self, region, stage, category, csv_file):
        
        mission_cards = []
        with open(csv_file) as csvfile:
            dreader = csv.DictReader(csvfile)
            for rowd in dreader:
                
                next_card = MissionCard(rowd, category)
                
                if region not in next_card.region:
                    continue
                
                if stage not in next_card.stage:
                    continue
                
                mission_cards.append(next_card)

        return mission_cards
    
    def top_trigger(self):
        
        if len(self.cards) > 0:
            return self.cards[0].trigger
        else:
            return "Empty"
        
    # Draw a number of cards equal to stage, return list of triggers
    def draw_triggers(self, stage):

        triggers = ["None", "None", "None"]
        
        if len(self.cards) < stage:
            return triggers, False
    
        for i in range(stage):   
            next_card = self.draw()
            next_trigger = next_card.trigger
            triggers[i] = next_trigger
            self.discard(next_card)
            
        return triggers
                  
          
if __name__ == "__main__":
    
    cdeck = MissionDeck('Empire', 'Starting', 
                        '../../csv/mission-cards-obstacles.csv',
                        '../../csv/mission-cards-scenes.csv',
                        '../../csv/mission-cards-twists.csv',
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