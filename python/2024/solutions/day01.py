#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def part_1(data):
    list_left = []
    list_right = []
    for left, right in map(str.split, data):
        list_left.append(int(left))
        list_right.append(int(right))
    list_left.sort()
    list_right.sort()
    answer = 0
    for left, right in zip(list_left, list_right):
        answer = answer + abs(left - right)
    return answer


def part_2(data):
    list_left = []
    list_right = {}
    for left, right in map(str.split, data):
        list_left.append(int(left))
        right_int = int(right)
        list_right[right_int] = list_right.get(right_int, 0) + 1
    return sum(list(map(lambda n: n * list_right.get(n, 0), list_left)))


sample_data = read_test_input(2024, 1)
data = read_input(2024, 1)

check(part_1(sample_data), 11)
print(part_1(data))

check(part_2(sample_data), 31)
print(part_2(data))
