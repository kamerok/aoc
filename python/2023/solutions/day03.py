#!/usr/bin/env python3
import re

from utils.utils import read_input, read_test_input, check


def is_symbol(data, row, col):
    if row < 0 or row >= len(data) or col < 0 or col >= len(data[0]):
        return False
    symbol = data[row][col]
    return symbol != '.'


def is_part_number(match, data, row):
    start = match.start(0)
    end = match.end(0)
    adjacent = []
    for col in range(start - 1, end + 1):
        adjacent.append((row - 1, col))
        adjacent.append((row + 1, col))

    adjacent.append((row, start - 1))
    adjacent.append((row, end))

    is_part_number = any([is_symbol(data, row, col) for row, col in adjacent])
    return is_part_number


def part_1(data):
    result = 0
    for i, line in enumerate(data):
        line_numbers = list(re.finditer(r'\d+', line))
        for match in line_numbers:
            if is_part_number(match, data, i):
                result = result + int(match[0])
    return result


def part_2(data):
    result = 0
    numbers_indexes = []
    for row, line in enumerate(data):
        line_numbers = list(re.finditer(r'\d+', line))
        for match in line_numbers:
            numbers_indexes.append([(row, col) for col in range(match.start(0), match.end(0))])
    for row, line in enumerate(data):
        for col, symbol in enumerate(line):
            if symbol == '*':
                adjacent = {(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                            (row, col - 1), (row, col + 1),
                            (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)}
                touching_numbers = list(filter(
                    lambda number_indexes: len(set(number_indexes) & adjacent) > 0,
                    numbers_indexes
                ))
                if len(touching_numbers) == 2:
                    numbers = list(map(lambda indexes: int(''.join(map(lambda i: data[i[0]][i[1]], indexes))), touching_numbers))
                    result = result + numbers[0] * numbers[1]
    return result


sample_data = read_test_input(2023, 3)
data = read_input(2023, 3)

check(part_1(sample_data), 4361)
print(part_1(data))

check(part_2(sample_data), 467835)
print(part_2(data))
