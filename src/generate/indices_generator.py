card_sets = [
    ['Empire Fronts', 1, 61],
    ['Empire Backs', 2, 61],
    ['Red Bank Fronts', 61, 121],
    ['Red Bank Backs', 62, 121],
    ['Settled Lands Fronts', 121, 183],
    ['Settled Lands Backs', 122, 183],
    ['Single Player Fronts', 1, 69],
    ['Single Player Backs', 2, 69],
    ['Two Player Fronts', 69, 175],
    ['Two Player Backs', 70, 175],
    ['Locations Fronts', 1, 67],
    ['Locations Backs', 2, 67],
    ['Weather Fronts', 1, 33],
    ['Weather Backs', 2, 33],
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
