card_sets = [
    ['Threat Mission Cards Fronts', 1, 129],
    ['Threat Mission Cards Backs', 2, 129],
    ['Attached Location Mission Cards Fronts', 129, 181],
    ['Attached Location Mission Cards Backs', 130, 181],
    ['Progress Fronts', 1, 103],
    ['Progress Backs', 2, 103],
    ['Locations Fronts', 1, 93],
    ['Locations Backs', 2, 93],
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
