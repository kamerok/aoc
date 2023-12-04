#!/usr/bin/env python3
import re

from utils.utils import read_input, read_test_input, check


def parse_tickets(data):
    def parse_ticket(line):
        num, winner = list(
            map(lambda s: set(map(int, re.findall(r'\d+', s))), line.partition(': ')[-1].split(' | ')))
        return {
            "num": num,
            "win": winner
        }

    return list(map(parse_ticket, data))


def get_matches(ticket):
    winner = ticket["win"]
    num = ticket["num"]
    power = len(num & winner)
    return power


def get_points(ticket):
    power = get_matches(ticket)
    if power > 0:
        return 2 ** (power - 1)
    else:
        return 0


def part_1(data):
    return sum(map(get_points, parse_tickets(data)))


def part_2(data):
    tickets = parse_tickets(data)
    numbers = [1 for _ in tickets]

    for ticket_index, ticket in enumerate(tickets):
        points = get_matches(ticket)
        for new_index in range(ticket_index + 1, ticket_index + 1 + points):
            if new_index < len(numbers):
                numbers[new_index] = numbers[new_index] + numbers[ticket_index]

    return sum(numbers)


sample_data = read_test_input(2023, 4)
data = read_input(2023, 4)

check(part_1(sample_data), 13)
print(part_1(data))

check(part_2(sample_data), 30)
print(part_2(data))
