# -*- coding: utf-8 -*-
"""
Deck of achievement cards.
"""

import csv

from deck import Deck

class AchievementCard:
    
    def __init__(self, cdict):

        self.region = cdict['region']
        self.stage = cdict['stage']        
        self.name = cdict['name']
        self.difficulty = cdict['difficulty']
        self.task = cdict['task']
        self.immediate = cdict['immediate']
        self.reward = cdict['reward']
        
    def __str__(self):
        cstring = self.name + ' ' + self.difficulty + \
            ' ' +self.task + ' ' + self.immediate + ' ' + self.reward
        return cstring
    
class AchievementDeck(Deck):
    
    def __init__(self, csv_file, region, stage):
        achievement_cards = []       
        with open(csv_file) as csvfile:
            dreader = csv.DictReader(csvfile)
            for rowd in dreader:
                
                next_card = AchievementCard(rowd)
                
                if region not in next_card.region:
                    continue
                
                if stage not in next_card.stage:
                    continue
                    
                achievement_cards.append(next_card)
        
        super().__init__(achievement_cards)
                  
          
if __name__ == "__main__":
    
    adeck = AchievementDeck('../../csv/achievement-cards.csv', 
                            'Empire', 'Starting')
    
    cc = adeck.draw()
    print('draw', cc)
    adeck.discard(cc)
    
    cc = adeck.draw()
    print('draw', cc)
    adeck.discard(cc)
    
    cc = adeck.draw()
    print('draw', cc)
    adeck.discard(cc)
    
    adeck.shuffle()
    
    cc = adeck.draw()
    print('draw', cc)
    adeck.discard(cc)
    
    cc = adeck.draw()
    print('draw', cc)
    adeck.discard(cc)
    
    cc = adeck.draw()
    print('draw', cc)
    adeck.discard(cc)

