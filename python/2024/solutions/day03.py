#!/usr/bin/env python3
import re

from utils.utils import read_input, read_test_input, check


def part_1(data):
    answer = 0
    matches = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', "".join(data))
    for m in matches:
        numbers = m[4:-1].split(',')
        answer = answer + int(numbers[0]) * int(numbers[1])
    return answer


def part_2(data):
    answer = 0
    matches = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)', "".join(data))
    skip = False
    for m in matches:
        if m == 'do()':
            skip = False
        elif m == 'don\'t()':
            skip = True
        elif not skip:
            numbers = m[4:-1].split(',')
            answer = answer + int(numbers[0]) * int(numbers[1])

    return answer


sample_data = read_test_input(2024, 3)
sample_data_2 = read_input(2024, 3, '_test2')
data = read_input(2024, 3)

check(part_1(sample_data), 161)
print(part_1(data))

check(part_2(sample_data_2), 48)
print(part_2(data))
