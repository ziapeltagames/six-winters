# -*- coding: utf-8 -*-
"""
Simple deck of trigger cards for timer analysis.
"""

import sys, csv

sys.path.append('../ui')

from deck import Deck


class TriggerCard:
    
    def __init__(self, cdict):
        
        self.region = cdict['region'] 
        self.trigger = cdict['trigger']     
        
    def __str__(self):
        cstring = self.region + ' ' + self.trigger
        return cstring
    
class TriggerDeck(Deck):
    
    def __init__(self, region, obstacles):
        
        mission_cards = []        
        mission_cards.extend(self.read_deck(region, obstacles))
        super().__init__(mission_cards)
        
    def read_deck(self, region, csv_file):
        
        mission_cards = []
        with open(csv_file) as csvfile:
            dreader = csv.DictReader(csvfile)
            for rowd in dreader:
                
                next_card = TriggerCard(rowd)
                
                if region not in next_card.region:
                    continue

                mission_cards.append(next_card)

        return mission_cards
          
if __name__ == "__main__":
    
    cdeck = TriggerDeck('Empire', 'trigger-cards.csv')
    
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