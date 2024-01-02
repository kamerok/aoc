#!/usr/bin/env python3
from enum import Enum

from utils.utils import read_input, check, read_test_input, a_star


class Direction(Enum):
    U = 1
    R = 2
    L = 3
    D = 4


def left(direction):
    match direction:
        case Direction.U:
            return Direction.L
        case Direction.R:
            return Direction.U
        case Direction.D:
            return Direction.R
        case Direction.L:
            return Direction.D


def right(direction):
    match direction:
        case Direction.U:
            return Direction.R
        case Direction.R:
            return Direction.D
        case Direction.D:
            return Direction.L
        case Direction.L:
            return Direction.U


def move(point, direction):
    row, col = point
    match direction:
        case Direction.U:
            return row - 1, col
        case Direction.R:
            return row, col + 1
        case Direction.D:
            return row + 1, col
        case Direction.L:
            return row, col - 1


def in_field(point, field):
    return 0 <= point[0] < len(field) and 0 <= point[1] < len(field[0])


def solve(field, min_steps, max_steps):
    start = ((0, 0), Direction.R.value, 0)
    end = (len(field) - 1, len(field[0]) - 1)

    def check_end(node):
        point, _, steps = node
        return point == end and steps >= min_steps

    def heuristic(node):
        (row, col), _, _ = node
        return (end[0] - row) + (end[1] - col)

    def distance(node):
        (row, col), _, _ = node
        return field[row][col]

    def neighbours(node):
        current_point, direction, steps = node
        direction = Direction(direction)
        candidates = []

        left_direction = left(direction)
        left_point = move(current_point, left_direction)
        candidates.append((left_point, left_direction, 1))

        right_direction = right(direction)
        right_point = move(current_point, right_direction)
        candidates.append((right_point, right_direction, 1))

        forward_point = move(current_point, direction)
        candidates.append((forward_point, direction, steps + 1))

        result = []
        for candidate_point, candidate_direction, candidate_steps in candidates:
            if not in_field(candidate_point, field):
                continue
            if candidate_steps > max_steps:
                continue
            if node != start and direction != candidate_direction and steps < min_steps:
                continue
            result.append((candidate_point, candidate_direction.value, candidate_steps))
        return result

    return a_star(start, check_end, distance, neighbours, heuristic)


def part_1(data):
    field = list(map(lambda line: list(map(int, list(line))), data))
    return solve(field, 0, 3)


def part_2(data):
    field = list(map(lambda line: list(map(int, list(line))), data))
    return solve(field, 4, 10)


sample_data = read_test_input(2023, 17)
sample_data_2 = read_input(2023, 17, '_test2')
data = read_input(2023, 17)

check(part_1(sample_data), 102)
print(part_1(data))

check(part_2(sample_data), 94)
check(part_2(sample_data_2), 71)
# 1027
print(part_2(data))
