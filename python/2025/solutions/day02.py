#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def part_1(data):
    ranges = list(map(lambda raw_range: raw_range.split('-'), data[0].split(',')))
    return sum(sum([find_symmetrical_matches(start, end) for start, end in ranges], []))


def find_symmetrical_matches(start, end):
    if len(start) % 2 > 0:
        start = pow(10, len(start))
    else:
        start = int(start)
    if len(end) % 2 > 0:
        end = pow(10, (len(end) - 1)) - 1
    else:
        end = int(end)

    if end < start:
        return []

    result = []
    half_start = int(f'{start}'[0:int(len(f'{start}')/2)])
    half_end = int(f'{end}'[0:int(len(f'{end}')/2)])
    for half in range(half_start, half_end + 1):
        number = int(f'{half}{half}')
        if number in range(start, end + 1):
            result.append(number)
    return result


def part_2(data):
    pass


sample_data = read_test_input(2025, 2)
data = read_input(2025, 2)

check(part_1(sample_data), 1227775554)
print(part_1(data))

check(part_2(sample_data), 4174379265)
print(part_2(data))
