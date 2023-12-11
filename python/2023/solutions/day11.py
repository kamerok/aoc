#!/usr/bin/env python3
import itertools
from itertools import combinations
from itertools import starmap

from utils.utils import read_input, read_test_input, check


def solve(data, expansion):
    expanded_rows = []
    for index, line in enumerate(data):
        if all(c == '.' for c in line):
            expanded_rows.append(index)

    expanded_columns = []
    for index in range(len(data[0])):
        if all(line[index] == '.' for line in data):
            expanded_columns.append(index)

    points = []
    for row_index, row in enumerate(data):
        for col_index, c in enumerate(row):
            if data[row_index][col_index] == '#':
                points.append((row_index, col_index))

    def find_distance(start, end):
        start_row = min(start[0], end[0])
        end_row = max(start[0], end[0])
        start_col = min(start[1], end[1])
        end_col = max(start[1], end[1])

        vertical = end_row - start_row
        horizontal = end_col - start_col
        for row in expanded_rows:
            if start_row <= row <= end_row:
                vertical = vertical + expansion - 1
        for col in expanded_columns:
            if start_col <= col <= end_col:
                horizontal = horizontal + expansion - 1
        return horizontal + vertical

    return sum(starmap(find_distance, combinations(points, 2)))


def part_1(data):
    return solve(data, 2)


def part_2(data, expansion):
    return solve(data, expansion)


sample_data = read_test_input(2023, 11)
data = read_input(2023, 11)

check(part_1(sample_data), 374)
print(part_1(data))

check(part_2(sample_data, 10), 1030)
check(part_2(sample_data, 100), 8410)
print(part_2(data, 1000000))
