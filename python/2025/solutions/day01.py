#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def part_1(data):
    instructions = [(line[0] == 'L', int(line[1:])) for line in data]
    current = 50
    zeroes = 0
    for is_left, steps in instructions:
        steps %= 100
        if is_left:
            current -= steps
            if current < 0:
                current += 100
        else:
            current += steps
            if current > 99:
                current %= 100
        zeroes += current == 0
    return zeroes


def part_2(data):
    instructions = [(line[0] == 'L', int(line[1:])) for line in data]
    current = 50
    zeroes = 0
    for is_left, steps in instructions:
        zeroes += int(steps / 100)
        steps %= 100
        if is_left:
            current -= steps
            if current < 0:
                zeroes += 1
                current += 100
        else:
            current += steps
            if current > 99:
                zeroes += 1
                current %= 100
    return zeroes


sample_data = read_test_input(2025, 1)
data = read_input(2025, 1)

check(part_1(sample_data), 3)
print(part_1(data))
check(part_1(data), 1154)

check(part_2(sample_data), 6)
print(part_2(data))
check(part_2(data), 6819)
