# -*- coding: utf-8 -*-
"""
Root class to handle card decks. Cards from decks can be in one of four
different states: draw pile, in play, discarded, or out of the game (burned).
"""

from random import shuffle

class Deck:
    
    # Cards are a list of objects
    def __init__(self, cards):
        self.discards = []
        self.cards = cards
        shuffle(self.cards)
    
    def draw_size(self):
        return len(self.cards)
    
    # Pull a card from the deck
    def draw(self):
        if self.cards:
            return self.cards.pop(0)
        else:
            return None
    
    def insert(self, card):
        self.cards.append(card)
    
    # Shuffle needs to take the draw pile and the discard pile
    def shuffle(self):
        self.cards.extend(self.discards)
        shuffle(self.cards)
        self.discards = []
    
    def discard_size(self):
        return len(self.discards)
        
    def discard(self, discarded):
        self.discards.append(discarded)
        