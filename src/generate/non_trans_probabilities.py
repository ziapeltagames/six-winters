from collections import Counter
import random

NUM_OF_TRIALS = 1000

red_die = [4, 4, 4, 4, 4, 9]
blue_die = [2, 2, 2, 7, 7, 7]
green_die = [5, 5, 5, 5, 5, 0]
yellow_die = [3, 3, 3, 3, 8, 8]
purple_die = [6, 6, 6, 6, 1, 1]

dice = [red_die, blue_die, green_die, yellow_die, purple_die]
die_names = ['Red', 'Blue', 'Green', 'Yellow', 'Purple']

def compare_two_dice(die1, die2):

    die1_wins = []
    die2_wins = []

    for i in range(NUM_OF_TRIALS):

        die1_score = random.choice(die1)
        die2_score = random.choice(die2)

        if die1_score > die2_score:
            die1_wins.append(die1_score - die2_score)
        else:
            die2_wins.append(die2_score - die1_score)

    return die1_wins, die2_wins

first_die = 2
print('Metrics For', die_names[first_die])

for second_die in range(len(die_names)):
    if second_die == first_die:
        continue

    print()
    print(die_names[first_die], 'vs', die_names[second_die])
    d1, d2 = compare_two_dice(dice[first_die], dice[second_die])

    print(die_names[first_die], 'wins:')
    for num, val in zip(Counter(d1).keys(), Counter(d1).values()):
        print(num, val/NUM_OF_TRIALS)

    print(die_names[second_die], 'wins:')
    for num, val in zip(Counter(d2).keys(), Counter(d2).values()):
        print(num, val/NUM_OF_TRIALS)