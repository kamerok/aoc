#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def mark_region(row, col, value, region, grid) -> (set, set):
    def is_the_same_region(new_row, new_col):
        return (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and
                grid[new_row][new_col] == value)

    borders = set()
    region.add((row, col))

    sides = (
        (0, -1, True, 0, 0),
        (-1, 0, False, 0, 0),
        (0, 1, True, 0, 1),
        (1, 0, False, 1, 0),
    )
    for dx, dy, is_side_vertical, side_dx, side_dy in sides:
        if (row + dx, col + dy) in region:
            pass
        elif is_the_same_region(row + dx, col + dy):
            local_region, local_borders = mark_region(row + dx, col + dy, value, region, grid)
            region.update(local_region)
            borders.update(local_borders)
        else:
            borders.add((is_side_vertical, row + side_dx, col + side_dy))

    return region, borders


def part_1(data):
    visited = set()
    answer = 0
    for row_index, row in enumerate(data):
        for col_index, value in enumerate(row):
            if (row_index, col_index) not in visited:
                region, borders = mark_region(row_index, col_index, data[row_index][col_index], set(), data)
                visited.update(region)
                answer = answer + len(region) * len(borders)
    return answer


def part_2(data):
    visited = set()
    answer = 0
    for row_index, row in enumerate(data):
        for col_index, value in enumerate(row):
            if (row_index, col_index) not in visited:
                region, borders = mark_region(row_index, col_index, data[row_index][col_index], set(), data)
                visited.update(region)

                straight_borders = 0
                in_border = False
                sorted_horizontal_borders = sorted([border for border in borders if not border[0]])
                for potential_border in sorted_horizontal_borders:
                    _, horizontal_index, vertical_index = potential_border
                    if not in_border:
                        straight_borders = straight_borders + 1
                        in_border = True
                    if (((True, horizontal_index - 1, vertical_index + 1) in borders and
                         (True, horizontal_index, vertical_index + 1) in borders) or
                            (False, horizontal_index, vertical_index + 1) not in borders):
                        in_border = False

                in_border = False
                sorted_horizontal_borders = sorted(
                    [border for border in borders if border[0]],
                    key=lambda b: (b[2], b[1])
                )
                for potential_border in sorted_horizontal_borders:
                    _, horizontal_index, vertical_index = potential_border
                    if not in_border:
                        straight_borders = straight_borders + 1
                        in_border = True
                    if (((False, horizontal_index + 1, vertical_index - 1) in borders and
                         (False, horizontal_index + 1, vertical_index) in borders) or
                            (True, horizontal_index + 1, vertical_index) not in borders):
                        in_border = False

                answer = answer + len(region) * straight_borders
    return answer


sample_data = read_test_input(2024, 12)
sample_data_2 = read_input(2024, 12, "_test2")
data = read_input(2024, 12)

check(part_1(sample_data), 1930)
print(part_1(data))

check(part_2(sample_data_2), 368)
check(part_2(sample_data), 1206)
print(part_2(data))
