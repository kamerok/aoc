#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def parse_prizes(data):
    prizes = []
    raw_prizes = list(map(lambda section: section.split('\n'), "\n".join(data).split("\n\n")))
    for button_a_raw, button_b_raw, prize_raw in raw_prizes:
        button_a = tuple(map(lambda s: int(s[2:]), button_a_raw[10:].split(', ')))
        button_b = tuple(map(lambda s: int(s[2:]), button_b_raw[10:].split(', ')))
        prize = tuple(map(lambda s: int(s[2:]), prize_raw[7:].split(', ')))
        prizes.append(dict(a=button_a, b=button_b, prize=prize))
    return prizes


def find_min_clicks(prize):
    a, b, prize = prize.values()
    # derived mathematically
    b_presses = (a[0]*prize[1] - prize[0]*a[1])/(a[0]*b[1] - b[0]*a[1])
    if b_presses % 1 == 0:
        a_presses = (prize[0] - b[0] * b_presses) / a[0]
        if a_presses % 1 == 0:
            return int(3 * a_presses + b_presses)
    return 0


def part_1(data):
    prizes = parse_prizes(data)
    return sum(map(find_min_clicks, prizes))


def part_2(data):
    prizes = parse_prizes(data)
    for prize in prizes:
        prize['prize'] = (prize['prize'][0] + 10000000000000, prize['prize'][1] + 10000000000000)
    return sum(map(find_min_clicks, prizes))


sample_data = read_test_input(2024, 13)
data = read_input(2024, 13)

check(part_1(sample_data), 480)
print(part_1(data))

print(part_2(data))
