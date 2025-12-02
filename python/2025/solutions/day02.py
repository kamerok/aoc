#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def part_1(data):
    ranges = list(map(lambda raw_range: raw_range.split('-'), data[0].split(',')))
    return sum(sum([find_symmetrical_matches(start, end, 2) for start, end in ranges], []))


def find_symmetrical_matches(start, end, base):
    if (mod := len(start) % base) > 0:
        start = pow(10, len(start) - 1 + (base - mod))
    else:
        start = int(start)
    if (mod := len(end) % base) > 0:
        end = pow(10, (len(end) - 1)) - mod
    else:
        end = int(end)

    if end < start:
        return []

    result = []
    part_start = int(f'{start}'[0:int(len(f'{start}') / base)])
    part_end = int(f'{end}'[0:int(len(f'{end}') / base)])
    for part in range(part_start, part_end + 1):
        number = int(f'{part}' * base)
        if number in range(start, end + 1):
            result.append(number)
    return result


def part_2(data):
    ranges = list(map(lambda raw_range: raw_range.split('-'), data[0].split(',')))
    result = 0
    for start, end in ranges:
        matches = []
        for base in range(2, max(len(start), len(end)) + 1):
            matches += find_symmetrical_matches(start, end, base)
        result += sum(set(matches))
    return result


sample_data = read_test_input(2025, 2)
data = read_input(2025, 2)

check(part_1(sample_data), 1227775554)
print(part_1(data))

check(part_2(sample_data), 4174379265)
print(part_2(data))
