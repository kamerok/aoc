#!/usr/bin/env python3

from utils.utils import read_input_raw, read_test_input_raw, check


def part_1(data):
    groups = data.split('\n\n')
    return sum(map(lambda group: len(set(group.replace('\n', ''))), groups))


def part_2(data):
    groups = [list(map(set, group.splitlines()))
              for group in data.split('\n\n')]

    return sum(len(set.intersection(*group)) for group in groups)


sample_data = read_test_input_raw(2020, 6)
data = read_input_raw(2020, 6)

check(part_1(sample_data), 11)
print(part_1(data))

check(part_2(sample_data), 6)
print(part_2(data))
