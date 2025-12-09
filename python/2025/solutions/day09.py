#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def part_1(data):
    points = [(x, y) for x, y in map(lambda line: map(int, line.split(',')), data)]
    areas = []
    for i, start in enumerate(points):
        for end in points[i + 1:]:
            areas.append(({start, end}, area(start, end)))
    areas.sort(key=lambda item: item[1])
    return areas[-1][1]


def area(start, end):
    return (abs(end[0] - start[0]) + 1) * (abs(end[1] - start[1]) + 1)


def part_2(data):
    points = [(x, y) for x, y in map(lambda line: map(int, line.split(',')), data)]
    points.append(points[0])

    x_slices = dict()
    y_slices = dict()
    for i in range(len(points) - 1):
        start = points[i]
        end = points[i + 1]
        if start[0] != end[0]:
            for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                is_corner = x == start[0] or x == end[0]
                x_slices[x] = x_slices.get(x, set()).union({(start[1], is_corner)})
        else:
            for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                is_corner = y == start[1] or y == end[1]
                y_slices[y] = y_slices.get(y, set()).union({(start[0], is_corner)})

    def join_slices_ranges(slices):
        for x, borders in slices.items():
            borders = list(borders)
            borders.sort(key=lambda item: item[0])
            filtered_borders = []
            for i, (value, is_corner) in enumerate(borders):
                if not is_corner or i == 0 or i == len(borders) - 1:
                    filtered_borders.append(value)
            borders = filtered_borders
            ranges = []
            for i in range(len(borders) - 1):
                ranges.append(range(borders[i], borders[i + 1] + 1))
            slices[x] = ranges

    join_slices_ranges(x_slices)
    join_slices_ranges(y_slices)

    areas = []
    for i, start in enumerate(points):
        for end in points[i + 1:]:
            areas.append(((start, end), area(start, end)))

    areas.sort(key=lambda item: item[1])
    areas.reverse()

    for (start, end), size in areas:
        side_x = range(min(start[0], end[0]), max(start[0], end[0]) + 1)
        side_y = range(min(start[1], end[1]), max(start[1], end[1]) + 1)

        if any(is_range_in_range(side_y, x_slice) for x_slice in x_slices[start[0]]):
            if any(is_range_in_range(side_y, x_slice) for x_slice in x_slices[end[0]]):
                if any(is_range_in_range(side_x, y_slice) for y_slice in y_slices[start[1]]):
                    if any(is_range_in_range(side_x, y_slice) for y_slice in y_slices[end[1]]):
                        return size

    return 0


def is_range_in_range(small, big):
    return small.start >= big.start and small.stop <= big.stop


sample_data = read_test_input(2025, 9)
data = read_input(2025, 9)

check(part_1(sample_data), 50)
print(part_1(data))

check(part_2(sample_data), 24)
print(part_2(data))
