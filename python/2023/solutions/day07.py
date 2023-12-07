#!/usr/bin/env python3
from functools import cmp_to_key
from itertools import starmap

from utils.utils import read_input, read_test_input, check


def part_1(data):
    order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    order.reverse()

    def compare(card1, card2):
        if card1['combo_power'] > card2['combo_power']:
            return 1
        elif card1['combo_power'] < card2['combo_power']:
            return -1
        for c1, c2 in zip(card1['combo'], card2['combo']):
            order1 = order.index(c1)
            order2 = order.index(c2)
            if order1 > order2:
                return 1
            elif order1 < order2:
                return -1
        return 0

    def parse_card(line):
        combo, score = line.split()
        letter_index_and_count = {c: (order.index(c), combo.count(c)) for c in combo}
        combo_size_to_number = {
            n: len(list(filter(lambda v: v[1] == n, letter_index_and_count.values()))) for n in [5, 4, 3, 2]
        }
        entries = [(k, v[0], v[1]) for k, v in letter_index_and_count.items()]
        entries.sort(key=lambda x: (x[2], x[1]), reverse=True)

        # 6 Five of a kind
        # 5 Four of a kind
        # 4 Full house
        # 3 Three of a kind
        # 2 Two pair
        # 1 One pair
        # 0 High card
        combo_power = 0
        if combo_size_to_number[5] > 0:
            combo_power = 6
        elif combo_size_to_number[4] > 0:
            combo_power = 5
        elif combo_size_to_number[3] > 0 and combo_size_to_number[2] > 0:
            combo_power = 4
        elif combo_size_to_number[3] > 0:
            combo_power = 3
        elif combo_size_to_number[2] > 1:
            combo_power = 2
        elif combo_size_to_number[2] > 0:
            combo_power = 1

        return dict(
            combo=combo,
            sorted_combo="".join(map(lambda entry: entry[0] * entry[2], entries)),
            combo_power=combo_power,
            score=int(score)
        )

    cards = list(map(parse_card, data))
    ordered = sorted(cards, key=cmp_to_key(compare))
    return sum(starmap(lambda i, card: (i + 1) * card['score'], enumerate(ordered)))


def part_2(data):
    order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    order.reverse()

    def compare(card1, card2):
        if card1['combo_power'] > card2['combo_power']:
            return 1
        elif card1['combo_power'] < card2['combo_power']:
            return -1
        for c1, c2 in zip(card1['combo'], card2['combo']):
            order1 = order.index(c1)
            order2 = order.index(c2)
            if order1 > order2:
                return 1
            elif order1 < order2:
                return -1
        return 0

    def parse_card(line):
        combo, score = line.split()
        wildcards = combo.count('J')
        reduced_combo = combo.replace('J', '')
        letter_index_and_count = {c: (order.index(c), reduced_combo.count(c)) for c in reduced_combo}
        combo_size_to_number = {
            n: len(list(filter(lambda v: v[1] == n, letter_index_and_count.values()))) for n in [5, 4, 3, 2, 1]
        }

        # 0 High card
        combo_power = 0

        # 6 Five of a kind
        if combo_size_to_number[5] > 0:
            combo_power = 6
        elif combo_size_to_number[4] > 0 and wildcards == 1:
            combo_power = 6
        elif combo_size_to_number[3] > 0 and wildcards == 2:
            combo_power = 6
        elif combo_size_to_number[2] > 0 and wildcards == 3:
            combo_power = 6
        elif combo_size_to_number[1] > 0 and wildcards == 4:
            combo_power = 6
        elif wildcards == 5:
            combo_power = 6

        # 5 Four of a kind
        elif combo_size_to_number[4] > 0:
            combo_power = 5
        elif combo_size_to_number[3] > 0 and wildcards >= 1:
            combo_power = 5
        elif combo_size_to_number[2] > 0 and wildcards >= 2:
            combo_power = 5
        elif combo_size_to_number[1] > 0 and wildcards >= 3:
            combo_power = 5
        elif wildcards >= 4:
            combo_power = 5

        # 4 Full house
        elif combo_size_to_number[3] > 0 and combo_size_to_number[2] > 0:
            combo_power = 4
        elif combo_size_to_number[2] > 1 and wildcards == 1:
            combo_power = 4

        # 3 Three of a kind
        elif combo_size_to_number[3] > 0:
            combo_power = 3
        elif combo_size_to_number[2] > 0 and wildcards == 1:
            combo_power = 3
        elif combo_size_to_number[1] > 0 and wildcards == 2:
            combo_power = 3
        elif wildcards >= 3:
            combo_power = 3

        # 2 Two pair
        elif combo_size_to_number[2] > 1:
            combo_power = 2

        # 1 One pair
        elif combo_size_to_number[2] > 0:
            combo_power = 1
        elif combo_size_to_number[1] > 0 and wildcards == 1:
            combo_power = 1
        elif wildcards == 2:
            combo_power = 1

        return dict(
            combo=combo,
            combo_power=combo_power,
            score=int(score)
        )

    cards = list(map(parse_card, data))
    ordered = sorted(cards, key=cmp_to_key(compare))
    return sum(starmap(lambda i, card: (i + 1) * card['score'], enumerate(ordered)))


sample_data = read_test_input(2023, 7)
data = read_input(2023, 7)

check(part_1(sample_data), 6440)
print(part_1(data))

check(part_2(sample_data), 5905)
print(part_2(data))
