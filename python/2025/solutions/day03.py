#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def part_1(data):
    return sum(map(lambda line: find_number(line, 2), data))


def find_number(line, base):
    numbers = [-1] * base
    for i, c in enumerate(line):
        candidate = int(c)
        for position, number in enumerate(numbers):
            if candidate > number and i < len(line) - (base - position - 1):
                numbers[position] = candidate
                for j in range(position + 1, base):
                    numbers[j] = -1
                break
    return int(''.join(map(str, numbers)))


def part_2(data):
    return sum(map(lambda line: find_number(line, 12), data))


sample_data = read_test_input(2025, 3)
data = read_input(2025, 3)

check(part_1(sample_data), 357)
print(part_1(data))

check(part_2(sample_data), 3121910778619)
print(part_2(data))
