#!/usr/bin/env python3

import os


def check(value, expected):
    assert value == expected, f'Expected {expected} but was {value}'


def read_input(year, day, suffix=''):
    return read_file_lines(get_file_path(year, day, suffix))


def read_input_raw(year, day, suffix=''):
    with open(get_file_path(year, day, suffix)) as file:
        return file.read()


def read_test_input(year, day):
    return read_input(year, day, '_test')


def read_test_input_raw(year, day):
    return read_input_raw(year, day, '_test')


def get_file_path(year, day, suffix=''):
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
