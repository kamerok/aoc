#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def part_1(data):
    start = data[0].find('S')
    row = 1
    beams = {start}
    splits = set()
    while row < len(data):
        new_beams = set()
        for col in beams:
            if data[row][col] == '.':
                new_beams.add(col)
            else:
                splits.add((row, col))
                new_beams.add(col - 1)
                new_beams.add(col + 1)
        row += 1
        beams = new_beams
    return len(splits)


def part_2(data):
    start = data[0].find('S')
    beams = {start: 1}
    row = 1
    while row < len(data):
        new_beams = dict()
        for col, options in beams.items():
            if data[row][col] == '.':
                new_beams[col] = new_beams.get(col, 0) + options
            else:
                new_beams[col - 1] = new_beams.get(col - 1, 0) + options
                new_beams[col + 1] = new_beams.get(col + 1, 0) + options
        row += 1
        beams = new_beams
    return sum(beams.values())


sample_data = read_test_input(2025, 7)
data = read_input(2025, 7)

check(part_1(sample_data), 21)
print(part_1(data))

check(part_2(sample_data), 40)
print(part_2(data))
