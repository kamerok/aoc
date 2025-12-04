#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def part_1(data):
    return len(find_cells_to_remove(data))


def find_cells_to_remove(data):
    to_remove = []
    for row, line in enumerate(data):
        for col, cell in enumerate(line):
            if cell == '@' and len(get_neighbours(row, col, data)) < 4:
                to_remove.append((row, col))
    return to_remove


def get_neighbours(row, col, data):
    neighbours = []
    for c_row in range(max(0, row - 1), min(len(data), row + 2)):
        for c_col in range(max(0, col - 1), min(len(data[0]), col + 2)):
            if (row, col) != (c_row, c_col) and data[c_row][c_col] == '@':
                neighbours.append((c_row, c_col))
    return neighbours


def part_2(data):
    data = [list(line) for line in data]
    removed = 0
    while len(to_remove := find_cells_to_remove(data)) > 0:
        removed += len(to_remove)
        for row, col in to_remove:
            data[row][col] = 'x'
    return removed


sample_data = read_test_input(2025, 4)
data = read_input(2025, 4)

check(part_1(sample_data), 13)
print(part_1(data))

check(part_2(sample_data), 43)
print(part_2(data))
