#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def part_1(data):
    instructions = [(line[0] == 'L', int(line[1:])) for line in data]
    current = 50
    zeroes = 0
    for is_left, steps in instructions:
        if is_left:
            current = current - steps % 100
            if current < 0:
                current = 100 + current
        else:
            current = current + steps
            if current > 99:
                current = current % 100
        if current == 0:
            zeroes = zeroes + 1
    return zeroes


def part_2(data):
    instructions = [(line[0] == 'L', int(line[1:])) for line in data]
    current = 50
    zeroes = 0
    for is_left, steps in instructions:
        if is_left:
            zeroes += int(steps / 100)
            current = current - steps % 100
            if current < 0:
                zeroes = zeroes + 1
                current = 100 + current
        else:
            current = current + steps
            zeroes = zeroes + int(current / 100)
            if current > 99:
                current = current % 100
    return zeroes
    pass


sample_data = read_test_input(2025, 1)
data = read_input(2025, 1)

check(part_1(sample_data), 3)
print(part_1(data))

check(part_2(sample_data), 6)
print(part_2(data))
