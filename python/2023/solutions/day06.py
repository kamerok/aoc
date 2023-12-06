#!/usr/bin/env python3
import re

from utils.utils import read_input, read_test_input, check


def part_1(data):
    races = list(zip(map(int, re.findall(r'\d+', data[0])), map(int, re.findall(r'\d+', data[1]))))
    result = 1
    for time, distance in races:
        options = map(lambda press: (time - press) * press, range(0, time))
        result = result * sum(1 for v in options if v > distance)
    return result


def part_2(data):
    (time, distance) = (int(data[0].split(':')[1].replace(' ', '')), int(data[1].split(':')[1].replace(' ', '')))
    options = map(lambda press: (time - press) * press, range(0, time))
    return sum(1 for v in options if v > distance)


sample_data = read_test_input(2023, 6)
data = read_input(2023, 6)

check(part_1(sample_data), 288)
print(part_1(data))
check(part_1(data), 128700)

check(part_2(sample_data), 71503)
print(part_2(data))
