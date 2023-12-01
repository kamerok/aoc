#!/usr/bin/env python3
import regex as re
from utils.utils import read_input, read_test_input, check


def part_1(data):
    def map_entry(entry):
        numbers = re.findall(r'\d', entry)
        return int(numbers[0] + numbers[-1])

    return sum(map(map_entry, data))


def part_2(data):
    word_numbers = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9',
    }
    words = [*word_numbers.keys()]

    def map_entry(entry):
        numbers = re.findall(r'\d|(?:{})'.format('|'.join(map(re.escape, words))), entry, overlapped=True)
        numbers = list(map(lambda n: word_numbers.get(n, n), numbers))
        number = numbers[0] + numbers[-1]
        return int(number)

    return sum(map(map_entry, data))


sample_data = read_test_input(2023, 1)
sample_data_2 = read_input(2023, 1, '_test2')
data = read_input(2023, 1)

check(part_1(sample_data), 142)
print(part_1(data))

check(part_2(sample_data_2), 281)
print(part_2(data))
