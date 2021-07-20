# -*- coding: utf-8 -*-
"""
Deck of location cards.
"""

import csv

from deck import Deck

class LocationCard:
    
    def __init__(self, cdict):

        self.region = cdict['region']
        self.stage = cdict['stage']        
        self.name = cdict['name']
        self.tags = cdict['tags']
        self.skill = cdict['skill']
        self.resource = cdict['resource']
        
    def __str__(self):
        cstring = self.name + ' ' + self.tags + \
            ' ' +self.skill + ' ' + self.resource
        return cstring
    
class LocationDeck(Deck):
    
    def __init__(self, csv_file, region, stage):
        location_cards = []       
        with open(csv_file) as csvfile:
            dreader = csv.DictReader(csvfile)
            for rowd in dreader:
                
                next_card = LocationCard(rowd)
                
                if region not in next_card.region:
                    continue
                
                if stage not in next_card.stage:
                    continue
                    
                location_cards.append(next_card)
        
        super().__init__(location_cards)
                  
          
if __name__ == "__main__":
    
    ldeck = LocationDeck('../../csv/location-cards.csv', 
                         'Empire', 'Starting')
    
    cc = ldeck.draw()
    print('draw', cc)
    ldeck.discard(cc)
    
    cc = ldeck.draw()
    print('draw', cc)
    ldeck.discard(cc)
    
    cc = ldeck.draw()
    print('draw', cc)
    ldeck.discard(cc)
    
    ldeck.shuffle()
    
    cc = ldeck.draw()
    print('draw', cc)
    ldeck.discard(cc)
    
    cc = ldeck.draw()
    print('draw', cc)
    ldeck.discard(cc)
    
    cc = ldeck.draw()
    print('draw', cc)
    ldeck.discard(cc)