#!/usr/bin/env python3
import functools

from utils.utils import read_input, read_test_input, check


@functools.cache
def count_options(row, number_input):
    if len(number_input) == 0:
        numbers = []
    else:
        numbers = list(map(int, number_input.split(',')))
    if len(numbers) > 0 and len(row) < numbers[0]:
        return 0
    if len(numbers) == 0:
        if '#' in row:
            return 0
        else:
            return 1

    matching_part = row[0:numbers[0]]
    if row[0] == '.':
        return count_options(row[1:], ",".join(map(str, numbers)))
    elif row[0] == '?':
        options_with_move = count_options(row[1:], ",".join(map(str, numbers)))
        if '.' not in matching_part and (len(row) == numbers[0] or row[numbers[0]] != '#'):
            return count_options(row[numbers[0] + 1:], ",".join(map(str, numbers[1:]))) + options_with_move
        else:
            return options_with_move
    elif row[0] == '#':
        if '.' not in matching_part and (len(row) == numbers[0] or row[numbers[0]] != '#'):
            return count_options(row[numbers[0] + 1:], ",".join(map(str, numbers[1:])))
        else:
            return 0


def part_1(data):
    result = 0
    for line in data:
        row, numbers = line.split(' ')
        result = result + count_options(row, numbers)
    return result


def part_2(data):
    result = 0
    for line in data:
        row, numbers = line.split(' ')
        duplicated_row = f'{row}?{row}?{row}?{row}?{row}'
        duplicated_numbers = f'{numbers},{numbers},{numbers},{numbers},{numbers}'
        result = result + count_options(duplicated_row, duplicated_numbers)
    return result


sample_data = read_test_input(2023, 12)
data = read_input(2023, 12)

check(count_options('???.###', '1,1,3'), 1)
check(part_1(sample_data), 21)
print(part_1(data))

check(part_2(sample_data), 525152)
print(part_2(data))
