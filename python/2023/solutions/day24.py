#!/usr/bin/env python3
from itertools import combinations

from utils.utils import read_input, check, read_test_input


def find_linear_arguments(hail):
    point, delta = hail
    x1, y1, _ = point
    x2 = x1 + delta[0]
    y2 = y1 + delta[1]
    return y2 - y1, x1 - x2, y1 * (x2 - x1) - (y2 - y1) * x1


def find_intersection(hail1, hail2):
    a1, b1, c1 = find_linear_arguments(hail1)
    a2, b2, c2 = find_linear_arguments(hail2)
    return (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1), (a2 * c1 - a1 * c2) / (a1 * b2 - a2 * b1)


def is_future_point(hail, xi, yi):
    point, delta = hail
    x1, y1, _ = point
    x2 = x1 + delta[0]
    y2 = y1 + delta[1]
    return abs(xi - x1) > abs(xi - x2) and abs(yi - y1) > abs(yi - y2)


def part_1(data, area_min, area_max):
    hails = tuple(
        (
            tuple(map(int, raw_point.split(', '))),
            tuple(map(int, raw_delta.split(', ')))
        )
        for raw_point, raw_delta
        in map(lambda line: line.split(' @ '), data)
    )
    answer = 0
    for hail1, hail2 in combinations(hails, 2):
        try:
            x, y = find_intersection(hail1, hail2)

            if (area_min <= x <= area_max and
                    area_min <= y <= area_max and
                    is_future_point(hail1, x, y) and
                    is_future_point(hail2, x, y)):
                answer = answer + 1
        except ZeroDivisionError:
            pass
    return answer


def part_2(data):
    return 0


sample_data = read_test_input(2023, 24)
input_data = read_input(2023, 24)

check(part_1(sample_data, 7, 27), 2)
print(part_1(input_data, 200000000000000, 400000000000000))

check(part_2(sample_data), 47)
print(part_2(input_data))
