#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def count_trails(data, row, col, current=0) -> list:
    if not 0 <= row < len(data) or not 0 <= col < len(data[0]):
        return []
    if current != int(data[row][col]):
        return []
    if current == 9 and data[row][col] == '9':
        return [(row, col)]
    trail_ends = (count_trails(data, row + 1, col, current + 1) +
                  count_trails(data, row - 1, col, current + 1) +
                  count_trails(data, row, col + 1, current + 1) +
                  count_trails(data, row, col - 1, current + 1))
    return trail_ends


def part_1(data):
    answer = 0
    for row_index, row in enumerate(data):
        for col_index, value in enumerate(row):
            if data[row_index][col_index] == '0':
                answer = answer + len(set(count_trails(data, row_index, col_index)))
    return answer


def part_2(data):
    answer = 0
    for row_index, row in enumerate(data):
        for col_index, value in enumerate(row):
            if data[row_index][col_index] == '0':
                answer = answer + len(count_trails(data, row_index, col_index))
    return answer


sample_data = read_test_input(2024, 10)
data = read_input(2024, 10)

check(part_1(sample_data), 36)
print(part_1(data))

check(part_2(sample_data), 81)
print(part_2(data))
