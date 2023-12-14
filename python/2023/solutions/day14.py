#!/usr/bin/env python3
import numpy as np

from utils.utils import read_input, read_test_input, check


def roll_north(field):
    for col in range(len(field[0])):
        index = 0
        for row in range(len(field)):
            if field[row][col] == 'O':
                if index != row:
                    field[index][col] = 'O'
                    field[row][col] = '.'
                index = index + 1
            elif field[row][col] == '#':
                index = row + 1


def roll_west(field):
    for row in range(len(field)):
        index = 0
        for col in range(len(field[0])):
            if field[row][col] == 'O':
                if index != col:
                    field[row][index] = 'O'
                    field[row][col] = '.'
                index = index + 1
            elif field[row][col] == '#':
                index = col + 1


def roll_south(field):
    for col in range(len(field[0])):
        index = len(field) - 1
        for row in reversed(range(len(field))):
            if field[row][col] == 'O':
                if index != row:
                    field[index][col] = 'O'
                    field[row][col] = '.'
                index = index - 1
            elif field[row][col] == '#':
                index = row - 1


def roll_east(field):
    for row in range(len(field)):
        index = len(field[0]) - 1
        for col in reversed(range(len(field[0]))):
            if field[row][col] == 'O':
                if index != col:
                    field[row][index] = 'O'
                    field[row][col] = '.'
                index = index - 1
            elif field[row][col] == '#':
                index = col - 1


def part_1(data):
    field = list(map(list, data))
    roll_north(field)

    result = 0
    for row, line in enumerate(field):
        result = result + line.count('O') * (len(field) - row)
    return result


def part_2(data):
    field = list(map(list, data))

    def cycle():
        roll_north(field)
        roll_west(field)
        roll_south(field)
        roll_east(field)

    def print_field():
        print("\n".join(map(''.join, field)))
        print()

    for _ in range(100):
        cycle()
    print_field()
    for _ in range(100):
        cycle()
    print_field()
    for _ in range(100):
        cycle()
    print_field()

    # for index in range(1_000_000_000):
    #     cycle()

    result = 0
    for row, line in enumerate(field):
        result = result + line.count('O') * (len(field) - row)
    return result


sample_data = read_test_input(2023, 14)
data = read_input(2023, 14)

check(part_1(sample_data), 136)
print(part_1(data))

check(part_2(sample_data), 64)
print(part_2(data))
