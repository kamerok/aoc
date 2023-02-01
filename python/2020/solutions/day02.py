#!/usr/bin/env python3

from itertools import combinations
import re
from utils.utils import read_input, read_test_input, check


class Entry:
    def __init__(self, line):
        min, max, char, pwd = re.split('-| |: ', line)
        self.min = int(min)
        self.max = int(max)
        self.char = char
        self.pwd = pwd

    def is_valid(self):
        return self.min <= self.pwd.count(self.char) <= self.max

    def is_valid_2(self):
        first = self.pwd[self.min - 1] == self.char
        second = self.pwd[self.max - 1] == self.char
        return first ^ second

def part_1(data):
    entries = list(map(Entry, data))
    return sum(entry.is_valid() for entry in entries)


def part_2(data):
    entries = list(map(Entry, data))
    return sum(entry.is_valid_2() for entry in entries)


sample_data = read_test_input(2020, 2)
data = read_input(2020, 2)

check(part_1(sample_data), 2)
print(part_1(data))

check(part_2(sample_data), 1)
print(part_2(data))
