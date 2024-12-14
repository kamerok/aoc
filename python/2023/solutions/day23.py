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


def find_nodes(data):
    nodes = {(1, 1), (len(data) - 2, len(data[0]) - 2)}
    for row in range(1, len(data) - 1):
        for col in range(1, len(data[0]) - 1):
            if data[row][col] == '#':
                continue
            neighbours = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            if len([p for p in neighbours if data[p[0]][p[1]] != '#']) > 2:
                nodes.add((row, col))
    return nodes


def part_2(data):
    nodes = find_nodes(data)
    graph = {}
    edges = {}

    scheduled = {(1, 1)}
    to_process = [((1, 1), (1, 2))]

    while to_process:
        start_node, current_point = to_process.pop()
        current_path = [start_node, current_point]

        def next_points():
            row, col = current_point
            neighbours = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            return [p for p in neighbours if p not in current_path and data[p[0]][p[1]] != '#']

        while len(next_points()) == 1:
            current_point = next_points()[0]
            current_path.append(current_point)

        assert current_point in nodes, 'Path is finished but not at node'
        graph[current_point] = {*graph.get(current_point, set()), start_node}
        graph[start_node] = {*graph.get(start_node, set()), current_point}
        edges[(start_node, current_point)] = len(current_path) - 1
        edges[(current_point, start_node)] = len(current_path) - 1
        if current_point not in scheduled:
            scheduled.add(current_point)
            for point in next_points():
                to_process.append((current_point, point))

    finish = (len(data) - 2, len(data[0]) - 2)

    def find_longest_route(current_node, length, visited):
        if current_node in visited:
            return 0

        visited = set(visited)
        visited.add(current_node)

        if current_node == finish:
            return length
        next_nodes = graph[current_node]
        if not next_nodes:
            return 0
        return max((find_longest_route(node, length + edges[(current_node, node)], visited) for node in next_nodes))

    return find_longest_route((1, 1), 0, set()) + 2


sample_data = read_test_input(2023, 23)
input_data = read_input(2023, 23)

check(part_1(sample_data), 94)
check(part_1(input_data), 2318)

check(part_2(sample_data), 154)
print(part_2(input_data))
