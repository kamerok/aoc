#!/usr/bin/env python3

import os


def check(value, expected):
    assert value == expected, f'Expected {expected} but was {value}'


def read_input(year, day):
    return read_file_lines(get_file_path(year, day, ''))


def read_input_raw(year, day):
    with open(get_file_path(year, day, '')) as file:
        return file.read()


def read_test_input(year, day):
    return read_file_lines(get_file_path(year, day, '_test'))


def read_test_input_raw(year, day):
    with open(get_file_path(year, day, '_test')) as file:
        return file.read()


def get_file_path(year, day, suffix):
    file_name = f'day{day:02d}{suffix}.txt'
    # notebook working directory support
    if os.getcwd().endswith('solutions'):
        return f'../inputs/{file_name}'
    else:
        return f'./python/{year}/inputs/{file_name}'


def read_file_lines(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines
