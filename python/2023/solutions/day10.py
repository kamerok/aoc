#!/usr/bin/env python3
from itertools import starmap

from utils.utils import read_input, read_test_input, check

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal
horizontal_right = ['S', '-', 'J', '7']
horizontal_left = ['S', 'F', 'L', '-']
vertical_bottom = ['S', '|', 'L', 'J']
vertical_top = ['S', '|', 'F', '7']


def part_1(data):
    data = list(map(list, data))
    start_row = next(filter(lambda tuple: 'S' in tuple[1], enumerate(data)))[0]
    start_column = data[start_row].index('S')

    queue = [(start_row, start_column)]
    while len(queue) > 0:
        row, col = queue.pop(0)
        current = data[row][col]
        data[row][col] = '*'
        # mark top
        if current in vertical_bottom and 0 <= row - 1 < len(data) and data[row - 1][col] in vertical_top:
            queue.append((row - 1, col))
        # mark bottom
        elif current in vertical_top and 0 <= row + 1 < len(data) and data[row + 1][col] in vertical_bottom:
            queue.append((row + 1, col))
        # mark left
        elif current in horizontal_right and 0 <= col - 1 < len(data[0]) and data[row][col - 1] in horizontal_left:
            queue.append((row, col - 1))
        # mark right
        elif current in horizontal_left and 0 <= col + 1 < len(data[0]) and data[row][col + 1] in horizontal_right:
            queue.append((row, col + 1))

    return round(sum(map(lambda line: line.count('*'), data)) / 2)


def part_2(data):
    original_data = list(map(list, data))
    data = list(map(list, data))
    start_row = next(filter(lambda tuple: 'S' in tuple[1], enumerate(data)))[0]
    start_column = data[start_row].index('S')

    path = [(start_row, start_column, None)]
    while len(path) < 2 or path[0][0] != path[-1][0] or path[0][1] != path[-1][1]:
        row, col, _ = path[-1]
        current = data[row][col]
        # go up
        if current in vertical_bottom and 0 <= row - 1 < len(data) and data[row - 1][col] in vertical_top \
                and (len(path) < 2 or row - 1 != path[-2][0] or col != path[-2][1]):
            path.append((row - 1, col, 'U'))
        # go down
        elif current in vertical_top and 0 <= row + 1 < len(data) and data[row + 1][col] in vertical_bottom \
                and (len(path) < 2 or row + 1 != path[-2][0] or col != path[-2][1]):
            path.append((row + 1, col, 'D'))
        # go left
        elif current in horizontal_right and 0 <= col - 1 < len(data[0]) and data[row][col - 1] in horizontal_left \
                and (len(path) < 2 or row != path[-2][0] or col - 1 != path[-2][1]):
            path.append((row, col - 1, 'L'))
        # go right
        elif current in horizontal_left and 0 <= col + 1 < len(data[0]) and data[row][col + 1] in horizontal_right:
            path.append((row, col + 1, 'R'))

    # clean field
    for row_index, row in enumerate(data):
        for col_index, value in enumerate(row):
            data[row_index][col_index] = '.'

    # touch right side area
    potential_right_side = []
    for row, col, bearing in path:
        data[row][col] = bearing
        symbol = original_data[row][col]
        # mark right side area
        if symbol == '|':
            if bearing == 'D':
                potential_right_side.append((row, col - 1))
            else:
                potential_right_side.append((row, col + 1))
        elif symbol == '-':
            if bearing == 'L':
                potential_right_side.append((row - 1, col))
            else:
                potential_right_side.append((row + 1, col))
        elif symbol == 'L':
            if bearing == 'D':
                potential_right_side.append((row, col - 1))
                potential_right_side.append((row + 1, col - 1))
                potential_right_side.append((row + 1, col))
        elif symbol == 'J':
            if bearing == 'R':
                potential_right_side.append((row + 1, col))
                potential_right_side.append((row + 1, col + 1))
                potential_right_side.append((row, col + 1))
        elif symbol == '7':
            if bearing == 'U':
                potential_right_side.append((row, col + 1))
                potential_right_side.append((row - 1, col + 1))
                potential_right_side.append((row - 1, col))
        elif symbol == 'F':
            if bearing == 'L':
                potential_right_side.append((row - 1, col))
                potential_right_side.append((row - 1, col - 1))
                potential_right_side.append((row, col - 1))

    points_to_mark = []
    for row, col in potential_right_side:
        if 0 <= row < len(data) and 0 <= col < len(data[0]) and data[row][col] == '.':
            points_to_mark.append((row, col))
            data[row][col] = '#'

    # fill right side area
    while len(points_to_mark) > 0:
        current_row, current_col = points_to_mark.pop(0)
        data[current_row][current_col] = '#'
        neighbours = starmap(lambda dr, dc: (current_row + dr, current_col + dc),
                             [(-1, 0), (1, 0), (0, 1), (0, -1)])
        for n_row, n_col in neighbours:
            if 0 <= n_row < len(data) and 0 <= n_col < len(data[0]) and data[n_row][n_col] == '.':
                data[n_row][n_col] = '#'
                points_to_mark.append((n_row, n_col))

    # find inner area
    inner_area = '#'
    if '#' in data[0] or '#' in data[-1]:
        inner_area = '.'

    return sum(map(lambda line: line.count(inner_area), data))


sample_data = read_test_input(2023, 10)
sample_data_2 = read_input(2023, 10, '_test2')
sample_data_3 = read_input(2023, 10, '_test3')
sample_data_4 = read_input(2023, 10, '_test4')
sample_data_5 = read_input(2023, 10, '_test5')
sample_data_6 = read_input(2023, 10, '_test6')
data = read_input(2023, 10)

check(part_1(sample_data), 4)
check(part_1(sample_data_2), 8)
print(part_1(data))

check(part_2(sample_data_3), 4)
check(part_2(sample_data_4), 4)
check(part_2(sample_data_5), 8)
check(part_2(sample_data_6), 10)
# not 423
print(part_2(data))
