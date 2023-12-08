#!/usr/bin/env python3
from functools import reduce
from math import lcm

from utils.utils import read_input, read_test_input, check


def part_1(data):
    instructions = data[0]

    def map_line(line):
        node_name, directions = line.split(" = ")
        return node_name, directions[1:-1].split(", ")

    nodes = {key: value for key, value in map(map_line, data[2:])}

    step = 0
    current_node = 'AAA'

    while current_node != 'ZZZ':
        direction = instructions[step % len(instructions)]
        step = step + 1
        if direction == 'L':
            current_node = nodes[current_node][0]
        else:
            current_node = nodes[current_node][1]

    return step


def part_2(data):
    instructions = data[0]

    def map_line(line):
        node_name, directions = line.split(" = ")
        return node_name, directions[1:-1].split(", ")

    nodes = {key: value for key, value in map(map_line, data[2:])}

    start_nodes = list(filter(lambda k: k[-1] == 'A', nodes.keys()))

    def find_first_end(node):
        step = 0
        current_node = node

        while current_node[-1] != 'Z':
            direction = instructions[step % len(instructions)]
            step = step + 1
            if direction == 'L':
                current_node = nodes[current_node][0]
            else:
                current_node = nodes[current_node][1]

        return step

    return reduce(lcm, map(find_first_end, start_nodes))


sample_data = read_test_input(2023, 8)
sample_data_2 = read_input(2023, 8, '_test2')
sample_data_3 = read_input(2023, 8, '_test3')
data = read_input(2023, 8)

check(part_1(sample_data), 2)
check(part_1(sample_data_2), 6)
print(part_1(data))

check(part_2(sample_data_3), 6)
print(part_2(data))
