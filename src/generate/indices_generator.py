card_sets = [
    ['Empire Fronts', 1, 33],
    ['Empire Backs', 2, 33],
    ['Red Bank Fronts', 33, 65],
    ['Red Bank Backs', 34, 65],
    ['Settled Lands Fronts', 65, 97],
    ['Settled Lands Backs', 66, 97],
    ['Staged Mission Cards Fronts', 1, 129],
    ['Staged Mission Cards Backs', 2, 129],
    ['Attached Mission Cards Fronts', 129, 181],
    ['Attached Mission Cards Backs', 130, 181],
    ['Progress Fronts', 1, 103],
    ['Progress Backs', 2, 103],
    ['Locations Fronts', 1, 93],
    ['Locations Backs', 2, 93],
    ['Seasonal Events Fronts', 1, 33],
    ['Seasonal Events Backs', 2, 33],
    ['Thea Front', 1, 33],
    ['Thea Back', 2, 33],
    ['Menas Front', 33, 65],
    ['Menas Back', 34, 65],
    ['Fuscus Front', 65, 97],
    ['Fuscus Back', 66, 97],
    ['Keel Front', 97, 129],
    ['Keel Back', 98, 129],
    ['Lucia Front', 129, 161],
    ['Lucia Back', 130, 161],
    ['Oniri Front', 161, 193],
    ['Oniri Back', 162, 193],
    ['Yasmina Front', 193, 225],
    ['Yasmina Back', 194, 225]
]

import sys

with open('D:\\\\Dropbox\\Ziapelta Games\\Games\\Six Winters\\Cards\\tts_card_indices.txt', 'w') as f:

    sys.stdout = f

    print('Card Indices')

    for cards in card_sets:
        print('\n')
        print(cards[0])
        for i in range(cards[1], cards[2], 2):
            if i == cards[1]:
                print(i, end='', sep='')
            else:
                print(',', i, end='', sep='')
