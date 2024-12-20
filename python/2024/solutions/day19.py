#!/usr/bin/env python3
from functools import lru_cache

from utils.utils import read_input, read_test_input, check, a_star


@lru_cache
def possible_combinations(design, patterns, current=''):
    if current == design:
        return 1

    remainder = design[len(current):]
    return sum(possible_combinations(design, patterns, current + pattern)
               for pattern in patterns
               if remainder.startswith(pattern))


def part_1(data):
    patterns = tuple(data[0].split(', '))
    designs = data[2:]
    return sum(possible_combinations(design, patterns) > 0 for design in designs)


def part_2(data):
    patterns = tuple(data[0].split(', '))
    designs = data[2:]
    return sum(possible_combinations(design, patterns) for design in designs)


sample_data = read_test_input(2024, 19)
input_data = read_input(2024, 19)

check(part_1(sample_data), 6)
print(part_1(input_data))

check(part_2(sample_data), 16)
print(part_2(input_data))
