#!/usr/bin/env python3
from utils.utils import read_input, check, read_test_input


def print_field(field):
    print('\n'.join(map(''.join, field)))


def build_graph(data):
    field = list(map(list, data))
    weights = {}
    edges = {}

    def get_next(point):
        row, col = point
        neighbours = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
        return next((point for point in neighbours if is_next(point)), None)

    def is_next(point):
        return field[point[0]][point[1]] == '.'

    def get_edges(point):
        row, col = point
        result = []
        if field[row + 1][col] == 'v':
            result.append((row + 2, col))
        if field[row - 1][col] == '^':
            result.append((row - 2, col))
        if field[row][col + 1] == '>':
            result.append((row, col + 2))
        if field[row][col - 1] == '<':
            result.append((row, col - 2))
        return result

    to_process = [(1, 1)]
    while to_process:
        start = to_process.pop()
        current = start
        weight = 0
        field[current[0]][current[1]] = '#'

        while get_next(current):
            current = get_next(current)
            weight = weight + 1
            field[current[0]][current[1]] = '#'

        local_edges = get_edges(current)
        edges[start] = local_edges
        if local_edges:
            weight = weight + 2
        weights[start] = weight
        to_process.extend([point for point in local_edges if point not in weights])
    return weights, edges


def part_1(data):
    weights, edges = build_graph(data)
    end = next(point for point in weights.keys() if len(edges[point]) == 0)

    def max_path(point):
        next_nodes = edges[point]
        if len(next_nodes) == 0:
            return weights[end]
        next_length = max(map(max_path, next_nodes))

        return weights[point] + next_length

    return max_path((1, 1)) + 2


def part_2(data):

    return 0


sample_data = read_test_input(2023, 23)
data = read_input(2023, 23)

check(part_1(sample_data), 94)
check(part_1(data), 2318)

check(part_2(sample_data), 154)
print(part_2(data))
