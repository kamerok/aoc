#!/usr/bin/env python3
from copy import deepcopy

from utils.utils import check, read_input, read_test_input

OCCUPIED, EMPTY, FLOOR = '#L.'


def main():
    sample_data = read_test_input(2020, 11)
    data = read_input(2020, 11)

    check(part_1(sample_data), 37)
    print(part_1(data))

    check(part_2(sample_data), 26)
    print(part_2(data))


def part_1(data):
    seat_tolerance = 4
    data = list(map(list, data))
    next_step = advance(data, count_occupied, seat_tolerance)
    while data != next_step:
        data = next_step
        next_step = advance(next_step, count_occupied, seat_tolerance)

    return sum(row.count(OCCUPIED) for row in data)


def part_2(data):
    seat_tolerance = 5
    data = list(map(list, data))
    next_step = advance(data, count_far_occupied, seat_tolerance)
    while data != next_step:
        data = next_step
        next_step = advance(next_step, count_far_occupied, seat_tolerance)

    return sum(row.count(OCCUPIED) for row in data)


def print_field(data):
    print('=============')
    for row in data:
        print(''.join(row))
    print('=============')


def advance(data, count_function, seat_tolerance):
    new_data = deepcopy(data)
    for row_index, row in enumerate(data):
        for col_index, value in enumerate(row):
            occupied = count_function(data, row_index, col_index)
            if value == EMPTY and occupied == 0:
                new_data[row_index][col_index] = OCCUPIED
            elif value == OCCUPIED and occupied >= seat_tolerance:
                new_data[row_index][col_index] = EMPTY

    return new_data


def count_occupied(data, row_index, col_index):
    deltas = (
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    )

    count = 0
    for row_delta, col_delta in deltas:
        candidate_row = row_index + row_delta
        candidate_col = col_index + col_delta
        if 0 <= candidate_row < len(data) and 0 <= candidate_col < len(data[0]):
            count += data[candidate_row][candidate_col] == OCCUPIED
    return count


def count_far_occupied(data, row_index, col_index):
    deltas = (
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    )

    count = 0
    for row_delta, col_delta in deltas:
        candidate_row = row_index + row_delta
        candidate_col = col_index + col_delta
        while 0 <= candidate_row < len(data) and 0 <= candidate_col < len(data[0]):
            cell = data[candidate_row][candidate_col]
            candidate_row += row_delta
            candidate_col += col_delta
            if cell == OCCUPIED:
                count += 1
                break
            elif cell == EMPTY:
                break
    return count


if __name__ == '__main__':
    main()
