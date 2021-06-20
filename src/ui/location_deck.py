# -*- coding: utf-8 -*-
"""
Deck of location cards.
"""

import csv

from deck import Deck

class LocationCard:
    
    def __init__(self, ldict):

        self.name = ldict['name']        
        self.skill = ldict['skill']
        self.front = ldict['front']
        self.region = ldict['region']
        self.years = ldict['years']
        self.achievement1 = ldict['achievement1']
        self.achievement2 = ldict['achievement2']
        
    def __str__(self):
        cstring = self.name + ' ' + self.skill + ' ' + self.front \
            + ' ' + self.achievement1 + ' ' + self.achievement2
        return cstring
    
class LocationDeck(Deck):
    
    def __init__(self, csv_file, region, year):
        location_cards = []       
        with open(csv_file) as csvfile:
            dreader = csv.DictReader(csvfile)
            for rowd in dreader:
                
                next_card = LocationCard(rowd)
                
                if region not in next_card.region:
                    continue
                
                if year not in next_card.years:
                    continue
                    
                location_cards.append(LocationCard(rowd))
        
        super().__init__(location_cards)
                  
          
if __name__ == "__main__":
    
    ldeck = LocationDeck('../../csv/location-cards.csv', 'Empire', '1')
    
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