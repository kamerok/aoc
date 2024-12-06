#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def part_1(data):
    obstacles, start = parse_input(data)
    visited = get_path(data, obstacles, start)
    return len({point for point, _ in visited})


def get_path(data, obstacles, position):
    direction = (-1, 0)
    turns = {
        (-1, 0): (0, 1),
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0),
    }
    visited = set()
    visited.add((position, direction))
    while True:
        new_row = position[0] + direction[0]
        new_col = position[1] + direction[1]
        if not 0 <= new_row < len(data) or not 0 <= new_col < len(data[0]):
            break
        if (new_row, new_col) in obstacles:
            direction = turns[direction]
            continue
        position = (new_row, new_col)
        if (position, direction) in visited:
            return None
        visited.add((position, direction))
    return visited


def part_2(data):
    obstacles, start = parse_input(data)
    original_path = get_path(data, obstacles, start)
    original_path.remove((start, (-1, 0)))
    answer = 0
    for point in {point for point, _ in original_path}:
        new_obstacles = set(obstacles)
        new_obstacles.add(point)
        if get_path(data, new_obstacles, start) is None:
            answer = answer + 1
    return answer


def parse_input(data):
    obstacles = set()
    for row_index, row in enumerate(data):
        for col_index, col in enumerate(row):
            if data[row_index][col_index] == '^':
                start = (row_index, col_index)
            if data[row_index][col_index] == '#':
                obstacles.add((row_index, col_index))
    return obstacles, start


sample_data = read_test_input(2024, 6)
data = read_input(2024, 6)

check(part_1(sample_data), 41)
print(part_1(data))

check(part_2(sample_data), 6)
print(part_2(data))
