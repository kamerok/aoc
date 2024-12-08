#!/usr/bin/env python3
from itertools import permutations, combinations

from utils.utils import read_input, read_test_input, check


def parse_antennas(data):
    antennas = {}
    for row_index, row in enumerate(data):
        for col_index, element in enumerate(row):
            if element == '.':
                continue
            else:
                element_set = antennas.get(element, set())
                element_set.add((row_index, col_index))
                antennas[element] = element_set
    return antennas


def part_1(data):
    antennas = parse_antennas(data)
    antinodes = {}
    for antenna, nodes in antennas.items():
        antinodes_set = set()
        for antenna1, antenna2 in combinations(nodes, 2):
            dx = antenna2[0] - antenna1[0]
            dy = antenna2[1] - antenna1[1]
            antinodes_set.add((antenna2[0] + dx, antenna2[1] + dy))
            antinodes_set.add((antenna1[0] - dx, antenna1[1] - dy))
        antinodes_set = {item for item in antinodes_set if 0 <= item[0] < len(data) and 0 <= item[1] < len(data[0])}
        antinodes[antenna] = antinodes_set
    return len({item for items in antinodes.values() for item in items})


def part_2(data):
    antennas = parse_antennas(data)
    antinodes = {}
    for antenna, nodes in antennas.items():
        antinodes_set = set()
        for antenna1, antenna2 in combinations(nodes, 2):
            dx = antenna2[0] - antenna1[0]
            dy = antenna2[1] - antenna1[1]

            def add_antinode_at_step(step):
                row = antenna1[0] + dx * step
                col = antenna1[1] + dy * step
                if 0 <= row < len(data) and 0 <= col < len(data[0]):
                    antinodes_set.add((row, col))
                    return True
                else:
                    return False

            step = 0
            while add_antinode_at_step(step):
                step = step + 1
            step = -1
            while add_antinode_at_step(step):
                step = step - 1
        antinodes[antenna] = antinodes_set
    return len({item for items in antinodes.values() for item in items})


sample_data = read_test_input(2024, 8)
data = read_input(2024, 8)

check(part_1(sample_data), 14)
print(part_1(data))

check(part_2(sample_data), 34)
print(part_2(data))
