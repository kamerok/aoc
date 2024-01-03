#!/usr/bin/env python3

from utils.utils import read_input, check, read_test_input


def solve(instructions):
    initial_points = [((0, 0), '', '')]
    current_point = (0, 0)

    for index in range(len(instructions)):
        direction, steps = instructions[index]
        next_index = index + 1 if index < len(instructions) - 1 else 0
        new_direction = instructions[next_index][0]
        match direction:
            case 'R':
                diff = (0, 1)
            case 'D':
                diff = (1, 0)
            case 'L':
                diff = (0, -1)
            case 'U':
                diff = (-1, 0)
        current_point = (
            current_point[0] + diff[0] * steps,
            current_point[1] + diff[1] * steps
        )
        initial_points.append((current_point, direction, new_direction))

    def adjust_point(entry):
        point, enter_direction, exit_direction = entry
        match enter_direction:
            case 'R':
                if exit_direction == 'U':
                    point = (point[0], point[1])
                else:
                    point = (point[0], point[1] + 1)
            case 'D':
                if exit_direction == 'R':
                    point = (point[0], point[1] + 1)
                else:
                    point = (point[0] + 1, point[1] + 1)
            case 'L':
                if exit_direction == 'U':
                    point = (point[0] + 1, point[1])
                else:
                    point = (point[0] + 1, point[1] + 1)
            case 'U':
                if exit_direction == 'L':
                    point = (point[0] + 1, point[1])
                else:
                    point = (point[0], point[1])

        return point

    points = list(map(adjust_point, initial_points))

    def map_index(i):
        next_index = i + 1 if i < (len(points) - 1) else 0
        y1, x1 = points[i]
        y2, x2 = points[next_index]
        return x1 * y2 - x2 * y1

    return sum(map(map_index, range(0, len(points)))) / 2


def part_1(data):
    def parse_instruction(line):
        split = line.split()
        return split[0], int(split[1])

    instructions = list(map(parse_instruction, data))
    return solve(instructions)


def part_2(data):
    def parse_instruction(line):
        to_parse = line.split()[2][2:-1]
        direction_index = int(to_parse[-1])
        directions = 'RDLU'
        return directions[direction_index], int(to_parse[:-1], 16)

    instructions = list(map(parse_instruction, data))
    return solve(instructions)


sample_data = read_test_input(2023, 18)
data = read_input(2023, 18)

check(part_1(sample_data), 62)
print(part_1(data))

check(part_2(sample_data), 952408144115)
print(part_2(data))
