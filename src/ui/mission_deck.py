# -*- coding: utf-8 -*-
"""
Deck of mission cards.
"""

import csv

from deck import Deck

class MissionCard:
    
    def __init__(self, mdict):

        self.location = mdict['location']        
        self.trigger = mdict['trigger']
        self.title = mdict['title']
        
    def __str__(self):
        cstring = self.location + ' ' + self.title
        return cstring
    
class MissionDeck(Deck):
    
    def __init__(self, csv_file):
        self.mission_cards = []
        with open(csv_file) as csvfile:
            dreader = csv.DictReader(csvfile)
            for rowd in dreader:
                self.mission_cards.append(MissionCard(rowd))
                
        super().__init__(self.mission_cards)
        
        
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
    
    cc = cdeck.draw()
    print('draw', cc)
    cdeck.discard(cc)
    
    cc = cdeck.draw()
    print('draw', cc)
    cdeck.discard(cc)
    
    cc = cdeck.draw()
    print('draw', cc)
    cdeck.discard(cc)