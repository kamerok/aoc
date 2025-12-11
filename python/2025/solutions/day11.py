#!/usr/bin/env python3
from functools import lru_cache

from utils.utils import read_input, read_test_input, check


def part_1(data):
    connections = parse_input(data)

    @lru_cache
    def count_paths(current):
        if current == 'out':
            return 1
        return sum(count_paths(n) for n in connections[current])

    return count_paths('you')


def parse_input(data):
    connections = dict()
    for line in data:
        start, raw_ends = line.split(': ')
        ends = raw_ends.split(' ')
        connections[start] = ends
    return connections


def part_2(data):
    connections = parse_input(data)

    @lru_cache(maxsize=1000000)
    def count_paths(current, visited_fft=False, visited_dac=False):
        visited_fft = visited_fft or current == 'fft'
        visited_dac = visited_dac or current == 'dac'
        if current == 'out':
            if visited_dac and visited_fft:
                return 1
            else:
                return 0
        return sum(count_paths(n, visited_fft, visited_dac) for n in connections[current])

    return count_paths('svr')


sample_data = read_test_input(2025, 11)
sample_data2 = read_input(2025, 11, '_test2')
data = read_input(2025, 11)

check(part_1(sample_data), 5)
print(part_1(data))

check(part_2(sample_data2), 2)
print(part_2(data))
