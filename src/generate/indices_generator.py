card_sets = [
    ['Empire Fronts', 1, 61],
    ['Empire Backs', 2, 61],
    ['Red Bank Fronts', 61, 121],
    ['Red Bank Backs', 62, 121],
    ['Settled Lands Fronts', 121, 183],
    ['Settled Lands Backs', 122, 183],
    ['Two Player Fronts', 69, 175],
    ['Two Player Backs', 70, 175]
]

for cards in card_sets:
    print('\n')
    print(cards[0])
    for i in range(cards[1], cards[2], 2):
        if i == cards[1]:
            print(i, end='', sep='')
        else:
            print(',', i, end='', sep='')

print('\n')
print('Thea')
print('1-6')

print('')
print('Menas')
print('17-22')

print('')
print('Fuscus')
print('33-38')

print('')
print('Keel')
print('49-54')