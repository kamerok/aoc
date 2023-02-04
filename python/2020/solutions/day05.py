#!/usr/bin/env python3


from utils.utils import read_input, check


def find_seat(code):
    table = code.maketrans('BFRL', '1010')
    return int(code.translate(table), 2)


def part_1(data):
    return max(list(map(find_seat, data)))


def part_2(data):
    seats = list(map(find_seat, data))
    min_seat = min(seats)
    max_seat = max(seats)
    return sum(range(min_seat, max_seat + 1)) - sum(seats)


data = read_input(2020, 5)

check(find_seat('FBFBBFFRLR'), 357)
check(find_seat('BFFFBBFRRR'), 567)
check(find_seat('FFFBBBFRRR'), 119)
check(find_seat('BBFFBBFRLL'), 820)
print(part_1(data))

print(part_2(data))
