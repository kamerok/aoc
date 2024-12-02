#!/usr/bin/env python3
from math import copysign

from utils.utils import read_input, read_test_input, check


def part_1(data):
    return sum(
        map(
            verify_report,
            map(lambda r: list(map(int, r.split())), data)
        )
    )


def verify_report(report, problem_dampener=False):
    # predict range direction
    decrease = 0
    increase = 0
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if copysign(1, diff) > 0:
            increase = increase + 1
        elif copysign(1, diff) < 0:
            decrease = decrease + 1
    if increase > decrease:
        range_sign = 1
    else:
        range_sign = -1

    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if copysign(1, diff) != range_sign or not 1 <= abs(diff) <= 3:
            if problem_dampener:
                without_left = list(report)
                del without_left[i - 1]
                without_right = list(report)
                del without_right[i]
                return verify_report(without_left) or verify_report(without_right)
            else:
                return False

    return True


def part_2(data):
    return sum(
        map(
            lambda report: verify_report(report, problem_dampener=True),
            map(lambda r: list(map(int, r.split())), data)
        )
    )


sample_data = read_test_input(2024, 2)
data = read_input(2024, 2)

check(part_1(sample_data), 2)
print(part_1(data))

check(part_2(sample_data), 4)
print(part_2(data))
