#!/usr/bin/env python3
from utils.utils import read_input, check, read_test_input


def part_1(data, steps):
    start_row_index, start_row = next((i, line) for i, line in enumerate(data) if 'S' in line)

    points = {(start_row_index, start_row.index('S'))}

    for _ in range(steps):
        new_points = set()
        for point in points:
            row, col = point
            candidates = ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1))
            for candidate in candidates:
                candidate_row, candidate_col = candidate
                if (0 <= candidate_row < len(data)
                        and 0 <= candidate_col < len(data[0])
                        and data[candidate_row][candidate_col] != '#'):
                    new_points.add(candidate)
        points = new_points

    return len(points)


def part_2(data, steps):
    start_row_index, start_row = next((i, line) for i, line in enumerate(data) if 'S' in line)

    points = {(start_row_index, start_row.index('S'))}

    for i in range(steps):
        new_points = set()
        for point in points:
            row, col = point
            candidates = ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1))
            for candidate in candidates:
                raw_candidate_row, raw_candidate_col = candidate
                candidate_row = raw_candidate_row % len(data)
                candidate_col = raw_candidate_col % len(data[0])
                if data[candidate_row][candidate_col] != '#':
                    new_points.add((raw_candidate_row, raw_candidate_col))
        points = new_points

    # points_normalized = set(map(lambda point: (point[0] % len(data), point[1] % len(data[0])), points))
    # field = list(map(list, data))
    # for row, col in points_normalized:
    #     field[row][col] = 'X'
    # for line in field:
    #     print(''.join(line))
    # print()

    return len(points)


sample_data = read_test_input(2023, 21)
data = read_input(2023, 21)

check(part_1(sample_data, 6), 16)
print(part_1(data, 64))

print(part_2(data, 65))
print(part_2(data, 196))
print(part_2(data, 327))
# use lagrange with 26501365 (https://www.dcode.fr/lagrange-interpolating-polynomial)
# day 9 could also be reused here (https://www.reddit.com/r/adventofcode/comments/18orn0s/comment/kgsaoi5/?utm_source=reddit&utm_medium=web2x&context=3)
