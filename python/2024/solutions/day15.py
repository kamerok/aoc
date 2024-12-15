#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def part_1(data):
    raw_field, raw_commands = '\n'.join(data).split('\n\n')
    commands = ''.join(raw_commands.split())
    field = raw_field.split()
    walls = set()
    boxes = set()
    robot = (-1, -1)
    for row_index, row in enumerate(field):
        for col_index, value in enumerate(row):
            if value == '#':
                walls.add((row_index, col_index))
            elif value == 'O':
                boxes.add((row_index, col_index))
            elif value == '@':
                robot = (row_index, col_index)

    directions = {
        '<': (0, -1),
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
    }

    def move(cell, delta):
        next_cell = (cell[0] + delta[0], cell[1] + delta[1])
        # next to the wall - don't move
        if next_cell in walls:
            return cell
        # next to the space - move and update global boxes if current is box
        elif next_cell not in boxes:
            if cell in boxes:
                boxes.remove(cell)
                boxes.add(next_cell)
            return next_cell
        # next to another box - try to move the box
        else:
            new_box_position = move(next_cell, delta)
            # box didn't move - don't move current
            if new_box_position == next_cell:
                return cell
            # box moved - try to move again
            else:
                return move(cell, delta)

    for command in commands:
        robot = move(robot, directions[command])

    return sum(row * 100 + col for row, col in boxes)


def part_2(data):
    raw_field, raw_commands = '\n'.join(data).split('\n\n')
    commands = ''.join(raw_commands.split())
    field = raw_field.split()
    walls = set()
    boxes = set()
    box_left = set()
    box_right = set()
    robot = (-1, -1)
    for row_index, line in enumerate(field):
        for col_index, value in enumerate(line):
            adjusted_col = col_index * 2
            adjusted_col_2 = col_index * 2 + 1
            if value == '#':
                walls.add((row_index, adjusted_col))
                walls.add((row_index, adjusted_col_2))
            elif value == 'O':
                boxes.add((row_index, adjusted_col))
                box_left.add((row_index, adjusted_col))
                boxes.add((row_index, adjusted_col_2))
                box_right.add((row_index, adjusted_col_2))
            elif value == '@':
                robot = (row_index, adjusted_col)

    def print_field():
        for row_index in range(len(field)):
            row = ''
            for col in range(len(field[0]) * 2):
                point = (row_index, col)
                if point in walls:
                    row = row + '#'
                elif point in box_left:
                    row = row + '['
                elif point in box_right:
                    row = row + ']'
                elif point == robot:
                    row = row + '@'
                else:
                    row = row + '.'
            print(row)
        print()

    def move_horizontally(cell, delta):
        next_cell = (cell[0], cell[1] + delta)
        # next to the wall - don't move
        if next_cell in walls:
            return cell
        # next to the space - move and update global boxes if current is box
        elif next_cell not in boxes:
            if cell in boxes:
                boxes.remove(cell)
                boxes.add(next_cell)
            if cell in box_left:
                box_left.remove(cell)
                box_left.add(next_cell)
            if cell in box_right:
                box_right.remove(cell)
                box_right.add(next_cell)
            return next_cell
        # next to another box - try to move the box
        else:
            new_box_position = move_horizontally(next_cell, delta)
            # box didn't move - don't move current
            if new_box_position == next_cell:
                return cell
            # box moved - try to move again
            else:
                return move_horizontally(cell, delta)

    def can_move_vertically(cell, delta):
        cells_to_move = []
        if cell not in walls and cell not in boxes:
            cells_to_move.append(cell)
        elif cell in box_left:
            cells_to_move.append(cell)
            cells_to_move.append((cell[0], cell[1] + 1))
        else:
            cells_to_move.append(cell)
            cells_to_move.append((cell[0], cell[1] - 1))
        new_cells = [(row + delta, col) for row, col in cells_to_move]

        # next to the wall - don't move
        if any(next_cell in walls for next_cell in new_cells):
            return False
        # next to the space - move and update global boxes if current is box
        elif all(next_cell not in boxes for next_cell in new_cells):
            return True
        # there is a box in the new points - try to move the box first
        else:
            occupied_cell = [cell for cell in new_cells if cell in boxes]
            return all(can_move_vertically(cell, delta) for cell in occupied_cell)

    def move_vertically(cell, delta):
        cells_to_move = []
        if cell not in walls and cell not in boxes:
            cells_to_move.append(cell)
        elif cell in box_left:
            cells_to_move.append(cell)
            cells_to_move.append((cell[0], cell[1] + 1))
        else:
            cells_to_move.append(cell)
            cells_to_move.append((cell[0], cell[1] - 1))
        new_cells = [(row + delta, col) for row, col in cells_to_move]

        # next to the wall - don't move
        if any(next_cell in walls for next_cell in new_cells) or not can_move_vertically(cell, delta):
            return cell
        # next to the space - move and update global boxes if current is box
        elif all(next_cell not in boxes for next_cell in new_cells):
            for cell, next_cell in zip(cells_to_move, new_cells):
                if cell in boxes:
                    boxes.remove(cell)
                    boxes.add(next_cell)
                if cell in box_left:
                    box_left.remove(cell)
                    box_left.add(next_cell)
                if cell in box_right:
                    box_right.remove(cell)
                    box_right.add(next_cell)
            return new_cells[0]
        # there is a box in the new points - try to move the box first
        else:
            occupied_cell = next(cell for cell in new_cells if cell in boxes)
            new_box_position = move_vertically(occupied_cell, delta)
            # box didn't move - don't move current
            if new_box_position == new_cells[0]:
                return cell
            # box moved - try to move again
            else:
                return move_vertically(cell, delta)

    for command in commands:
        if command == '<':
            robot = move_horizontally(robot, -1)
        elif command == '>':
            robot = move_horizontally(robot, 1)
        if command == '^':
            robot = move_vertically(robot, -1)
        elif command == 'v':
            robot = move_vertically(robot, 1)

    return sum(row * 100 + col for row, col in box_left)


sample_data = read_test_input(2024, 15)
sample_data2 = read_input(2024, 15, suffix='_test2')
input_data = read_input(2024, 15)

check(part_1(sample_data), 2028)
check(part_1(sample_data2), 10092)
print(part_1(input_data))

check(part_2(sample_data2), 9021)
print(part_2(input_data))
