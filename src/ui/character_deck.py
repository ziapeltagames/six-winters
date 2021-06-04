# -*- coding: utf-8 -*-
"""
Deck of character cards for chance resolution.
"""

import csv

from deck import Deck

class CharacterCard:
    
    def __init__(self, cdict):
        
        self.name = cdict['name']
        self.effect1 = cdict['effect1']
        self.effect2 = cdict['effect2']
        
    def __str__(self):
        cstring = self.name + ' ' + self.effect1 + ' ' + self.effect2
        return cstring
    
class CharacterDeck(Deck):
    
    def __init__(self, csv_file):
        self.character_cards = []
        with open(csv_file) as csvfile:
            dreader = csv.DictReader(csvfile)
            for rowd in dreader:
                self.character_cards.append(CharacterCard(rowd))
                
        super().__init__(self.character_cards)
        
        
if __name__ == "__main__":
    
    cdeck = CharacterDeck('../../csv/thea-deck.csv')
    
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
    print('draw', cc.name, cc.effect1, cc.effect2)
    cdeck.discard(cc)