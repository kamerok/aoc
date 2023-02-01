#!/usr/bin/env python3

from itertools import count
from utils.utils import read_input, read_test_input, check


def count_trees(data, row_step, col_step):
    height = len(data)
    width = len(data[0])

    trees = 0
    for row, col in zip(range(0, height, row_step), count(0, col_step)):
        if data[row][col % width] == '#':
            trees += 1
    return trees


def part_1(data):
    trees = count_trees(data, 1, 3)
    return trees


def part_2(data):
    result = 1

    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    for col_step, row_step in slopes:
        result *= count_trees(data, row_step, col_step)

    return result


sample_data = read_test_input(2020, 3)
data = read_input(2020, 3)

check(part_1(sample_data), 7)
print(part_1(data))

check(part_2(sample_data), 336)
print(part_2(data))
