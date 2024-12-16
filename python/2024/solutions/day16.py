#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check, a_star_path


def distance(current_node, next_node):
    current_point, current_direction = current_node
    next_point, next_direction = next_node
    if current_point == next_point:
        # rotation
        return 1000
    else:
        return 1


rotations_clockwise = {
    (-1, 0): (0, 1),
    (0, -1): (-1, 0),
    (1, 0): (0, -1),
    (0, 1): (1, 0),
}
rotations_counterclockwise = {
    (0, 1): (-1, 0),
    (-1, 0): (0, -1),
    (0, -1): (1, 0),
    (1, 0): (0, 1),
}


def neighbours(node, data):
    point, direction = node
    result = [(point, rotations_clockwise[direction]), (point, rotations_counterclockwise[direction])]
    row = point[0] + direction[0]
    col = point[1] + direction[1]
    if data[row][col] in '.E':
        result.append(((row, col), direction))
    return result


def find_shortest_path(data):
    start = ((len(data) - 2, 1), (0, 1))
    end = (1, len(data[0]) - 2)

    def check_end(node):
        point, _ = node
        return point == end

    def heuristic(node):
        (row, col), _ = node
        return (end[0] - row) + (end[1] - col)

    return a_star_path(start, check_end, distance, lambda node: neighbours(node, data), heuristic)


def calculate_path_length(path, data):
    start = ((len(data) - 2, 1), (0, 1))
    length = distance(start, path[0])
    for i in range(len(path) - 1):
        length = length + distance(path[i], path[i + 1])
    return length


def part_1(data):
    return calculate_path_length(find_shortest_path(data), data)


def part_2(data):
    min_length = calculate_path_length(find_shortest_path(data), data)

    cache = {}

    def find_min_paths(position, path, length, target):
        if cache.get(position, target) < length:
            return [set()]
        else:
            cache[position] = length

        if length > target:
            return [set()]
        if position[0] == (1, len(data[0]) - 2) and length == target:
            return [path]

        paths = []
        candidates = neighbours(position, data)
        next_nodes = []
        for node in candidates:
            (row, col), (dx, dy) = node
            if node[0] == position[0]:
                if data[row + dx][col + dy] == '#':
                    continue
            if node not in path:
                next_nodes.append(node)
        for next_node in next_nodes:
            new_path = {*path, next_node}
            paths.extend(find_min_paths(next_node, new_path, length + distance(position, next_node), target))

        return paths

    start = ((len(data) - 2, 1), (0, 1))
    points = set()
    for path in find_min_paths(start, [start], 0, min_length):
        for p, _ in path:
            points.add(p)
    return len(points)


sample_data = read_test_input(2024, 16)
sample_data2 = read_input(2024, 16, suffix='_test2')
input_data = read_input(2024, 16)

check(part_1(sample_data), 7036)
check(part_1(sample_data2), 11048)
print(part_1(input_data))

check(part_2(sample_data), 45)
check(part_2(sample_data2), 64)
print(part_2(input_data))
