#!/usr/bin/env python3
from collections import deque

from utils.utils import check, read_test_input, read_input


def main():
    sample_data = tuple(map(int, read_test_input(2020, 9)))
    data = tuple(map(int, read_input(2020, 9)))

    check(part_1(sample_data, 5), 127)
    print(part_1(data, 25))

    check(part_2(sample_data, 5), 62)
    print(part_2(data, 25))


def part_1(data, preamble_count):
    preamble = deque()

    def is_sum(number):
        for n in preamble:
            if (number - n) in preamble:
                return True
        return False

    for i in range(preamble_count):
        preamble.append(data[i])
    for i in range(preamble_count, len(data)):
        number = data[i]
        if is_sum(number):
            preamble.popleft()
            preamble.append(number)
        else:
            return number


def part_2(data, preamble_count):
    number = part_1(data, preamble_count)
    sum_range = find_sum_range(data, number)
    return min(sum_range) + max(sum_range)


def find_sum_range(data, number):
    start = 0
    end = 1
    current_sum = data[0]
    while current_sum != number:
        if current_sum > number:
            current_sum -= data[start]
            start += 1
        else:
            current_sum += data[end]
            end += 1
    return data[start:end]


if __name__ == '__main__':
    main()
