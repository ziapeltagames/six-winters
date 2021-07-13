# -*- coding: utf-8 -*-
"""
Deck of location cards.
"""

import csv

from deck import Deck

class LocationCard:
    
    def __init__(self, ldict):

        print(ldict)
        
        self.name = ldict['name']        
        self.skill = ldict['skill']
        self.society = ldict['society']
        self.region = ldict['region']
        self.trigger = ldict['trigger']
        self.tags = ldict['tags']
        
    def __str__(self):
        cstring = self.name + ' ' + self.skill + ' ' + self.society + \
            ' ' +self.tags + ' ' + self.trigger
        return cstring
    
class LocationDeck(Deck):
    
    def __init__(self, csv_file, region):
        location_cards = []       
        with open(csv_file) as csvfile:
            dreader = csv.DictReader(csvfile)
            for rowd in dreader:
                
                next_card = LocationCard(rowd)
                
                if region not in next_card.region:
                    continue
                    
                location_cards.append(LocationCard(rowd))
        
        super().__init__(location_cards)
                  
          
if __name__ == "__main__":
    
    ldeck = LocationDeck('../../csv/location-cards.csv', 'Empire')
    
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