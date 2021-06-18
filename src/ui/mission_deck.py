# -*- coding: utf-8 -*-
"""
Deck of mission cards.
"""

import csv

from deck import Deck

class MissionCard:
    
    def __init__(self, mdict):

        self.region = mdict['region']        
        self.trigger = mdict['trigger']
        self.title = mdict['title']
        
    def __str__(self):
        cstring = self.region + ' ' + self.title
        return cstring
    
class MissionDeck(Deck):
    
    def __init__(self, csv_file):
        mission_cards = []
        self.region_names = []        
        with open(csv_file) as csvfile:
            dreader = csv.DictReader(csvfile)
            for rowd in dreader:
                
                next_card = MissionCard(rowd)
                
                if next_card.region not in self.region_names:
                    self.region_names.append(next_card.region)
                    
                mission_cards.append(MissionCard(rowd))
                
        super().__init__(mission_cards)
        
    # Retrieve all of the possible characters
    def regions(self):
        return self.region_names
    
    # Use only the listed characters, with given commitment and discord
    # levels, in the deck
    def filter_regions(self, r1):
        
        trimmed_regions = []
        
        for mc in self.cards:
            
            if mc.region == r1:
                trimmed_regions.append(mc)               
        
        self.region_names = [r1]
        self.cards = trimmed_regions
        
    def get_trigger(self):
        
        if len(self.cards) > 0:
            return self.cards[0].trigger
        else:
            return "Empty"
        
        
if __name__ == "__main__":
    
    cdeck = MissionDeck('../../csv/mission-cards.csv')
    
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
    
    cdeck.filter_regions("Empire")
    
    cc = cdeck.draw()
    print('draw', cc)
    cdeck.discard(cc)
    
    cc = cdeck.draw()
    print('draw', cc)
    cdeck.discard(cc)
    
    cc = cdeck.draw()
    print('draw', cc)
    cdeck.discard(cc)