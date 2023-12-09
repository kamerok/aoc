#!/usr/bin/env python3
import re

from utils.utils import read_input, read_test_input, check


def parse(data):
    return list(map(lambda line: list(map(int, re.findall(r'-?\d+', line))), data))


def get_last_diff(sequence):
    next_line = list(map(lambda i: sequence[i + 1] - sequence[i], range(0, len(sequence) - 1)))
    if all(x == 0 for x in next_line):
        return 0
    else:
        diff = get_last_diff(next_line)
        return next_line[-1] + diff


def part_1(data):
    data = parse(data)
    return sum(map(lambda sequence: sequence[-1] + get_last_diff(sequence), data))


def get_new_first_item(sequence):
    next_line = list(map(lambda i: sequence[i + 1] - sequence[i], range(0, len(sequence) - 1)))
    if all(x == 0 for x in next_line):
        return sequence[0]
    else:
        diff = get_new_first_item(next_line)
        return sequence[0] - diff


def part_2(data):
    data = parse(data)
    return sum(map(lambda sequence: get_new_first_item(sequence), data))


sample_data = read_test_input(2023, 9)
data = read_input(2023, 9)

check(part_1(sample_data), 114)
print(part_1(data))

check(part_2(sample_data), 2)
print(part_2(data))
