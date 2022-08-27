card_sets = [
    ['Threat Obstcle Cards Fronts', 1, 123],
    ['Threat Obstcle Cards Backs', 2, 123],
    ['Attached Location Obstcle Cards Fronts', 123, 181],
    ['Attached Location Obstcle Cards Backs', 124, 181],
    ['Progress Fronts', 1, 103],
    ['Progress Backs', 2, 103],
    ['Locations Fronts', 1, 99],
    ['Locations Backs', 2, 99],
    ['Seasonal Events Fronts', 1, 33],
    ['Seasonal Events Backs', 2, 33]
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
