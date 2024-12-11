#!/usr/bin/env python3
from functools import lru_cache

from utils.utils import read_input, read_test_input, check


@lru_cache(maxsize=1000000)
def count_value_increase(value, count) -> int:
    if count == 0:
        return 1
    string_value = f"{value}"
    if value == 0:
        return count_value_increase(1, count - 1)
    elif len(string_value) % 2 == 0:
        left = int(string_value[:int(len(string_value) / 2)])
        right = int(string_value[int(len(string_value) / 2):])
        return count_value_increase(left, count - 1) + count_value_increase(right, count - 1)
    else:
        return count_value_increase(value * 2024, count - 1)


def part_1(data):
    data = list(map(int, data[0].split()))
    return sum(map(lambda n: count_value_increase(n, 25), data))


def part_2(data):
    data = list(map(int, data[0].split()))
    return sum(map(lambda n: count_value_increase(n, 75), data))


sample_data = read_test_input(2024, 11)
data = read_input(2024, 11)

check(part_1(sample_data), 55312)
print(part_1(data))

print(part_2(data))
