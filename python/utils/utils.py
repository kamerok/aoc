#!/usr/bin/env python3

def check(value, expected):
    assert value == expected, f'Expected {expected} but was {value}'

def read_input(year, day):
    return read_file(f'./python/{year}/inputs/day{day:02d}.txt')

def read_test_input(year, day):
    return read_file(f'./python/{year}/inputs/day{day:02d}_test.txt')

def read_file(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines