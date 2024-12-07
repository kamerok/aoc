#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def compute_answer(data, include_concat=False):
    answer = 0
    for line in data:
        raw_sum, raw_numbers = line.split(':')
        total = int(raw_sum)
        values = tuple(map(int, raw_numbers.split()))
        if check_possibility(total, values, 0, values[0], include_concat):
            answer = answer + total
    return answer


def check_possibility(total, values, index, subtotal, include_concat=False):
    if subtotal > total:
        return False
    if index == len(values) - 1:
        if total == subtotal:
            return True
        else:
            return False
    next_value = values[index + 1]
    to_check = [subtotal + next_value, subtotal * next_value]
    if include_concat:
        to_check.append(int(f"{subtotal}{next_value}"))
    return any([check_possibility(total, values, index + 1, subtotal, include_concat) for subtotal in to_check])


def part_1(data):
    return compute_answer(data)


def part_2(data):
    return compute_answer(data, True)


sample_data = read_test_input(2024, 7)
data = read_input(2024, 7)

check(part_1(sample_data), 3749)
print(part_1(data))

check(part_2(sample_data), 11387)
print(part_2(data))
