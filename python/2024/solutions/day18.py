#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check, a_star


def find_path(size, walls):
    start = (0, 0)
    end = (size - 1, size - 1)

    def check_end(node):
        return node == end

    def find_neighbours(node):
        x, y = node
        candidates = ((x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y))
        return [point for point in candidates if point not in walls and 0 <= point[0] < size and 0 <= point[1] < size]

    def heuristics(node):
        return (size - 1 - node[0]) + (size - 1 - node[1])

    return a_star(start, check_end, lambda p1, p2: 1, find_neighbours, heuristics)


def part_1(data, size):
    walls = set((int(x), int(y)) for x, y in map(lambda line: line.split(','), data))
    return find_path(size, walls)


def part_2(data, size):
    original_walls = [(int(x), int(y)) for x, y in map(lambda line: line.split(','), data)]
    walls = set()
    point = (0, 0)
    while find_path(size, walls):
        point = original_walls.pop(0)
        walls.add(point)
    return f'{point[0]},{point[1]}'


sample_data = read_test_input(2024, 18)
input_data = read_input(2024, 18)

check(part_1(sample_data[:12], 7), 22)
print(part_1(input_data[:1024], 71))

check(part_2(sample_data, 7), '6,1')
print(part_2(input_data, 71))
