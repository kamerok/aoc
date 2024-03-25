#!/usr/bin/env python3
from utils.utils import read_input, check, read_test_input, dijkstra


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
        return 0 <= point[0] < len(field) and 0 <= point[1] <= len(field[0]) and field[point[0]][point[1]] == '.'

    def get_edges(point):
        row, col = point
        result = []
        if 0 <= row + 1 < len(field) and field[row + 1][col] == 'v':
            result.append((row + 2, col))
        if 0 <= row - 1 < len(field) and field[row - 1][col] == '^':
            result.append((row - 2, col))
        if 0 <= col + 1 <= len(field[0]) and field[row][col + 1] == '>':
            result.append((row, col + 2))
        if 0 <= col - 1 <= len(field[0]) and field[row][col - 1] == '<':
            result.append((row, col - 2))
        return result

    to_process = [(0, 1)]
    while to_process:
        node = to_process.pop()
        current = node
        weight = 0
        field[current[0]][current[1]] = '#'

        while get_next(current):
            current = get_next(current)
            weight = weight + 1
            field[current[0]][current[1]] = '#'

        local_edges = get_edges(current)
        edges[node] = local_edges
        if local_edges:
            weight = weight + 2
        weights[node] = weight
        to_process.extend([point for point in local_edges if point not in weights])
    return weights, edges


def part_1(data):
    weights, edges = build_graph(data)
    end = next(point for point in weights.keys() if len(edges[point]) == 0)

    def max_path(point):
        if point == end:
            return weights[end]

        next_nodes = edges[point]
        next_length = max(map(max_path, next_nodes))

        return weights[point] + next_length

    return max_path((0, 1))


def part_2(data):

    return 0


sample_data = read_test_input(2023, 23)
data = read_input(2023, 23)

check(part_1(sample_data), 94)
print(part_1(data))

check(part_2(sample_data), 154)
print(part_2(data))
