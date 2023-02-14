#!/usr/bin/env python3
from collections import deque

from utils.utils import check, read_test_input, read_input


def main():
    sample_data_small = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    sample_data_large = [
        28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23,
        49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3
    ]
    data = list(map(int, read_input(2020, 10)))

    check(part_1(sample_data_small), 35)
    check(part_1(sample_data_large), 220)
    print(part_1(data))

    check(part_2(sample_data_small), 8)
    check(part_2(sample_data_large), 19208)
    print(part_2(data))


def part_1(data):
    data = list(data)
    data.sort()
    data.insert(0, 0)
    data.append(data[-1] + 3)

    diffs = {}
    for cur, nxt in zip(data, data[1:]):
        diff = nxt - cur
        diffs[diff] = diffs.get(diff, 0) + 1
    return diffs[1] * diffs[3]


def part_2(data):
    data = list(data)
    data.sort()
    data.insert(0, 0)
    data.append(data[-1] + 3)

    return count_options(0, data, {})


def count_options(index, data, cache):
    if index in cache:
        return cache[index]

    n = len(data)
    if index == n - 1:
        return 1

    options = 0

    possible_routes = (index + 1, index + 2, index + 3)
    for possible_next in possible_routes:
        if possible_next < n and data[possible_next] - data[index] <= 3:
            options += count_options(possible_next, data, cache)

    cache[index] = options
    return options


if __name__ == '__main__':
    main()
