# -*- coding: utf-8 -*-
"""
Deck of character cards.
"""

import csv

from deck import Deck

class CharacterCard:
    
    def __init__(self, cdict):
        
        self.category = cdict['category']
        self.name = cdict['name']
        self.effect1 = cdict['effect1']
        self.effect2 = cdict['effect2']
        
    def __str__(self):
        cstring = self.name + ' ' + self.effect1 + ' ' + self.effect2
        return cstring
    
class CharacterDeck(Deck):
    
    def __init__(self, csv_file):
        character_cards = []
        
        self.character_names = []
        self.trait_names = []
        
        with open(csv_file) as csvfile:
            dreader = csv.DictReader(csvfile)
            for rowd in dreader:
                
                next_card = CharacterCard(rowd)
                
                if next_card.category == "Character" \
                    and next_card.name not in self.character_names:
                        self.character_names.append(next_card.name)
                    
                if next_card.category == 'Trait' \
                    and next_card.name not in self.trait_names:
                        self.trait_names.append(next_card.name)
                        
                # Ignoring traits for now
                if next_card.category == 'Trait':
                    continue
                
                character_cards.append(next_card)
                
        super().__init__(character_cards)
        
    # Retrieve all of the possible characters
    def characters(self):
        return self.character_names
    
    # Use only the listed characters, with given commitment and discord
    # levels, in the deck
    def filter_characters(self, ch1, com1, dis1, ch2, com2, dis2):
        
        trimmed_characters = []
        
        for cc in self.cards:
            
            if cc.category == "Character":
                if cc.name == ch1 or cc.name == ch2:
                    trimmed_characters.append(cc)
            else:
                trimmed_characters.append(cc)                
        
        self.character_names = [ch1, ch2]
        self.cards = trimmed_characters
        
if __name__ == "__main__":
    
    cdeck = CharacterDeck('../../csv/character-cards.csv')
    
    chars = cdeck.characters()
    print("Characters", chars)
    
    cdeck.filter_characters(chars[0], 0, 0, chars[1], 0, 0)
    
    chars = cdeck.characters()
    print("Characters", chars)
    
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