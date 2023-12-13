#!/usr/bin/env python3
import functools
from itertools import starmap

from utils.utils import read_input, read_test_input, check


def check_vertical_symmetry(pivot, col_index, field):
    size_to_check = min(pivot + 1, len(field) - (pivot + 1))
    top_range = range(pivot + 1 - size_to_check, pivot + 1)
    bottom_range = reversed(range(pivot + 1, pivot + 1 + size_to_check))
    return all(field[t][col_index] == field[b][col_index] for t, b in zip(top_range, bottom_range))


def check_horizontal_symmetry(pivot, row_index, field):
    size_to_check = min(pivot + 1, len(field[0]) - (pivot + 1))
    left_range = range(pivot + 1 - size_to_check, pivot + 1)
    right_range = reversed(range(pivot + 1, pivot + 1 + size_to_check))
    return all(field[row_index][l] == field[row_index][r] for l, r in zip(left_range, right_range))


def find_symmetry_line(field):
    for vertical in range(len(field) - 1):
        if all(check_vertical_symmetry(vertical, col, field) for col in range(len(field[0]))):
            return None, vertical

    for horizontal in range(len(field[0]) - 1):
        if all(check_horizontal_symmetry(horizontal, row, field) for row in range(len(field))):
            return horizontal, None

    return None, None


def find_symmetry_lines(field):
    lines = []
    for vertical in range(len(field) - 1):
        if all(check_vertical_symmetry(vertical, col, field) for col in range(len(field[0]))):
            lines.append((None, vertical))

    for horizontal in range(len(field[0]) - 1):
        if all(check_horizontal_symmetry(horizontal, row, field) for row in range(len(field))):
            lines.append((horizontal, None))

    return lines


def part_1(data):
    fields = list(map(str.split, list("\n".join(data).split('\n\n'))))

    def calculate_points(vertical, horizontal):
        points = 0
        if horizontal is not None:
            points = (horizontal + 1) * 100
        elif vertical is not None:
            points = points + vertical + 1
        return points

    return sum(starmap(calculate_points, map(find_symmetry_line, fields)))


# ..#....#.
# ..######.
# ..###.##.
# ####..###
# ...####..
# ###.##.##
# ##.####.#
# ...#..#..
# ..######.

def fix_smudge(field):
    original_reflection = find_symmetry_line(field)
    for row in range(len(field)):
        for col in range(len(field[0])):
            new_field = list(map(list, field))
            if new_field[row][col] == '.':
                new_field[row][col] = '#'
            else:
                new_field[row][col] = '.'
            new_field = list(map(''.join, new_field))
            symmetry = find_symmetry_lines(new_field)
            new_reflections = list(filter(lambda r: r != original_reflection, symmetry))
            if len(new_reflections) > 0:
                return new_field, new_reflections[0]
    return field


def part_2(data):
    fields = list(map(str.split, list("\n".join(data).split('\n\n'))))

    def calculate_points(vertical, horizontal):
        points = 0
        if horizontal is not None:
            points = (horizontal + 1) * 100
        elif vertical is not None:
            points = points + vertical + 1
        return points

    fields = list(map(fix_smudge, fields))

    return sum(starmap(calculate_points, map(lambda f: f[1], fields)))


sample_data = read_test_input(2023, 13)
data = read_input(2023, 13)

check(part_1(sample_data), 405)
print(part_1(data))

# not 39697
check(part_2(sample_data), 400)
print(part_2(data))
