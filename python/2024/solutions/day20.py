#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check, a_star_path


def solve(data, min_save, cheats_allowed):
    start = end = None
    for row_index, row in enumerate(data):
        if 'S' in row:
            start = (row_index, row.index('S'))
        if 'E' in row:
            end = (row_index, row.index('E'))

    def find_neighbours(node):
        row, col = node
        return [(new_row, new_col) for new_row, new_col
                in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1))
                if data[new_row][new_col] != '#']

    path = a_star_path(start, lambda n: n == end, lambda p, c: 1, find_neighbours, lambda n: 0)
    path.insert(0, start)
    path_set = set(path)
    distances = {p: i for i, p in enumerate(path)}

    cheats = []
    cheats_buckets = {}

    diffs = ((1, 0), (-1, 0), (0, 1), (0, -1))
    for i, cheat_start in enumerate(path):
        visited = {}
        to_visit = [(cheat_start, 0)]
        while to_visit:
            current, steps = to_visit.pop()

            if steps > cheats_allowed:
                continue

            if not (0 <= current[0] < len(data) and 0 <= current[1] < len(data[0])):
                continue

            if current in visited and visited[current] <= steps:
                continue
            visited[current] = steps

            candidates = [(current[0] + d_row, current[1] + d_col) for d_row, d_col in diffs]
            for candidate in candidates:
                to_visit.append((candidate, steps + 1))

        for point, steps in visited.items():
            if point in path_set:
                old_distance = distances[point]
                new_distance = distances[cheat_start] + steps
                skip = old_distance - new_distance
                if skip >= min_save:
                    cheats.append((cheat_start, point))
                    cheats_buckets[skip] = cheats_buckets.get(skip, 0) + 1

    return len(cheats)


def part_1(data, min_save):
    return solve(data, min_save, 2)


def part_2(data, min_save):
    return solve(data, min_save, 20)


sample_data = read_test_input(2024, 20)
input_data = read_input(2024, 20)

check(part_1(sample_data, 1), 44)
print(part_1(input_data, 100))

check(part_2(sample_data, 50), 285)
print(part_2(input_data, 100))
