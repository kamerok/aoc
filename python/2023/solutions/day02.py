#!/usr/bin/env python3
import re

from utils.utils import read_input, read_test_input, check


def parse(data):
    def map_line(line):
        round_strings = line[line.index(':') + 2:len(line)].split('; ')
        game = {
            'id': int(line[5:line.index(':')]),
            'rounds': [{
                'red': int(next(iter(re.findall(r'(\d+) red', round_string)), 0)),
                'green': int(next(iter(re.findall(r'(\d+) green', round_string)), 0)),
                'blue': int(next(iter(re.findall(r'(\d+) blue', round_string)), 0))
            } for round_string in round_strings]
        }
        return game

    return [map_line(line) for line in data]


def part_1(data):
    games = parse(data)
    possible_games = list(filter(
        lambda game: all(
            round['red'] <= 12 and round['green'] <= 13 and round['blue'] <= 14
            for round in game['rounds']
        ),
        games
    ))
    return sum(map(lambda game: game['id'], possible_games))


def part_2(data):
    games = parse(data)

    def get_power(game):
        red, green, blue = 0, 0, 0
        for round in game['rounds']:
            red = max(round['red'], red)
            green = max(round['green'], green)
            blue = max(round['blue'], blue)
        return red * green * blue

    return sum(map(get_power, games))


sample_data = read_test_input(2023, 2)
data = read_input(2023, 2)

check(part_1(sample_data), 8)
print(part_1(data))

check(part_2(sample_data), 2286)
print(part_2(data))
