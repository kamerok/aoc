#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def part_1(data):
    keys = []
    locks = []
    groups = "\n".join(data).split('\n\n')
    for group in groups:
        grid = group.split()
        first_symbol = grid[0][0]
        mapping = []
        for col in range(len(grid[0])):
            count = 0
            for row in range(len(grid)):
                if grid[row][col] == first_symbol:
                    count = count + 1
            mapping.append(len(grid) - 1 - count)
        if first_symbol == '.':
            keys.append(mapping)
        else:
            locks.append(mapping)

    answer = 0
    for key in keys:
        for lock in locks:
            if all(l >= k for k, l in zip(key, lock)):
                answer = answer + 1
    return answer


sample_data = read_test_input(2024, 25)
input_data = read_input(2024, 25)

check(part_1(sample_data), 3)
print(part_1(input_data))
