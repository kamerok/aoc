#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def part_1(data):
    points = [(x, y) for x, y in map(lambda line: map(int, line.split(',')), data)]
    areas = sort_areas(points)
    return areas[-1][1]


def sort_areas(points):
    areas = []
    for i, start in enumerate(points):
        for end in points[i + 1:]:
            areas.append(({start, end}, area(start, end)))
    areas.sort(key=lambda item: item[1])
    return areas


def area(start, end):
    return (abs(end[0] - start[0]) + 1) * (abs(end[1] - start[1]) + 1)


def part_2(data):
    return 0


sample_data = read_test_input(2025, 9)
data = read_input(2025, 9)

check(part_1(sample_data), 50)
print(part_1(data))

# check(part_2(sample_data), 25272)
# print(part_2(data))
