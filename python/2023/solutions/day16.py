#!/usr/bin/env python3
from enum import Enum
from itertools import starmap

from utils.utils import read_input, check, read_test_input


class Direction(Enum):
    U = 1
    R = 2
    L = 3
    D = 4


def advance_point(row, col, direction):
    match direction:
        case Direction.L:
            return row, col - 1, direction
        case Direction.R:
            return row, col + 1, direction
        case Direction.U:
            return row - 1, col, direction
        case Direction.D:
            return row + 1, col, direction


def energize(start, data, longest_processed):
    processed = []
    to_process = [start]
    while len(to_process) > 0:
        point = to_process.pop(0)
        if point in longest_processed and len(processed) < 5:
            return 0
        row, col, direction = point
        is_valid = 0 <= row < len(data) and 0 <= col < len(data[0])
        if is_valid and point not in processed:
            processed.append(point)
            cell_value = data[row][col]
            match cell_value:
                case '.':
                    to_process.append(advance_point(row, col, direction))
                case '\\':
                    match direction:
                        case Direction.L:
                            new_direction = Direction.U
                        case Direction.R:
                            new_direction = Direction.D
                        case Direction.U:
                            new_direction = Direction.L
                        case Direction.D:
                            new_direction = Direction.R
                    to_process.append(advance_point(row, col, new_direction))
                case '/':
                    match direction:
                        case Direction.L:
                            new_direction = Direction.D
                        case Direction.R:
                            new_direction = Direction.U
                        case Direction.U:
                            new_direction = Direction.R
                        case Direction.D:
                            new_direction = Direction.L
                    to_process.append(advance_point(row, col, new_direction))
                case '-':
                    match direction:
                        case Direction.L | Direction.R:
                            to_process.append(advance_point(row, col, direction))
                        case Direction.U | Direction.D:
                            to_process.append(advance_point(row, col, Direction.L))
                            to_process.append(advance_point(row, col, Direction.R))
                case '|':
                    match direction:
                        case Direction.U | Direction.D:
                            to_process.append(advance_point(row, col, direction))
                        case Direction.L | Direction.R:
                            to_process.append(advance_point(row, col, Direction.U))
                            to_process.append(advance_point(row, col, Direction.D))

    if len(processed) > len(longest_processed):
        longest_processed.clear()
        longest_processed.extend(processed)
    return len(set(map(lambda point: (point[0], point[1]), processed)))


def part_1(data):
    return energize((0, 0, Direction.R), data, [])


def part_2(data):
    starts = []
    for row in range(len(data)):
        starts.append((row, 0, Direction.R))
        starts.append((row, len(data[0]) - 1, Direction.L))
    for col in range(len(data[0])):
        starts.append((0, col, Direction.D))
        starts.append((len(data) - 1, col, Direction.U))

    longest_processed = []

    def mapper(index, start):
        return energize(start, data, longest_processed)

    return max(starmap(mapper, enumerate(starts)))


sample_data = read_test_input(2023, 16)
data = read_input(2023, 16)

check(part_1(sample_data), 46)
check(part_1(data), 6816)
print(part_1(data))

check(part_2(sample_data), 51)
check(part_2(data), 8163)
print(part_2(data))
