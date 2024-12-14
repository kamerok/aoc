#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def parse_robots(data):
    return tuple(map(
        lambda line: tuple(map(
            lambda raw_point: tuple(map(int, raw_point[2:].split(','))),
            line.split()
        )),
        data
    ))


def move_robot(robot, steps, width, height):
    position, delta = robot
    x, y = position
    dx, dy = delta
    nx = x + dx * steps
    ny = y + dy * steps
    return (nx % width, ny % height), delta


def print_field(robots, width, height):
    print(field_to_string(robots, width, height))


def field_to_string(robots, width, height):
    positions = {robot[0] for robot in robots}
    output = ''
    for y in range(width):
        row = ''
        for x in range(height):
            if (x, y) in positions:
                row = row + '#'
            else:
                row = row + '.'
        output = output + row + '\n'
    return output


def count_quadrants(robots, width, height):
    q1, q2, q3, q4 = 0, 0, 0, 0
    for robot in robots:
        position = robot[0]
        if 0 <= position[0] < int(width / 2):
            if 0 <= position[1] < int(height / 2):
                q1 = q1 + 1
            elif int(height / 2) < position[1] < height:
                q3 = q3 + 1
        elif int(width / 2) < position[0] < width:
            if 0 <= position[1] < int(height / 2):
                q2 = q2 + 1
            elif int(height / 2) < position[1] < height:
                q4 = q4 + 1
    return q1, q2, q3, q4


def part_1(data, width, height):
    robots = parse_robots(data)

    moved_robots = tuple(move_robot(robot, 100, width, height) for robot in robots)

    q1, q2, q3, q4 = count_quadrants(moved_robots, width, height)
    return q1 * q2 * q3 * q4


def part_2(data, width, height):
    robots = parse_robots(data)

    for i in range(100000000):
        robots = tuple(move_robot(robot, 1, width, height) for robot in robots)

        field_render = field_to_string(robots, width, height)
        if '########' in field_render:
            print(field_render)
            print(i + 1)
            break


sample_data = read_test_input(2024, 14)
input_data = read_input(2024, 14)

check(part_1(sample_data, 11, 7), 12)
print(part_1(input_data, 101, 103))

part_2(input_data, 101, 103)
