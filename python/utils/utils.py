#!/usr/bin/env python3

def check(value, expected):
    assert value == expected, f'Expected {expected} but was {value}'

def read_input(year, day):
    return open(f'./python/{year}/inputs/day{day:02d}.txt').readlines()

def read_test_input(year, day):
    return open(f'./python/{year}/inputs/day{day:02d}_test.txt').readlines()