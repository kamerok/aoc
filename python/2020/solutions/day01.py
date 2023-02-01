#!/usr/bin/env python3

from itertools import combinations
from utils.utils import read_input, read_test_input, check


def part_1(data):
    for x in data:
        y = 2020 - x
        if y in data:
            return x * y


def part_2(data):
    for x, y in combinations(data, 2):
        z = 2020 - x - y
        if (z in data):
            return x * y * z


sample_data = set(map(int, read_test_input(2020, 1)))
data = set(map(int, read_input(2020, 1)))

check(part_1(sample_data), 514579)
print(part_1(data))

check(part_2(sample_data), 241861950)
print(part_2(data))
