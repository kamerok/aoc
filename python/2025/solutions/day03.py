#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def part_1(data):
    return sum(map(find_number, data))


def find_number(line):
    first = -1
    second = -1
    for i, c in enumerate(line):
        number = int(c)
        if number > first and i < (len(line) - 1):
            first = number
            second = -1
        elif number > second:
            second = number
    return int(f'{first}{second}')


def part_2(data):
    pass


sample_data = read_test_input(2025, 3)
data = read_input(2025, 3)

check(part_1(sample_data), 357)
print(part_1(data))

check(part_2(sample_data), 3121910778619)
print(part_2(data))
