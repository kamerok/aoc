#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def part_1(data):
    machines = parse_input(data)
    answer = 0
    for target, buttons, _ in machines:
        answer += find_shortest_combo(target, buttons)
    return answer


def parse_input(data):
    machines = []
    for line in data:
        items = line.split(' ')
        lights = [c == '#' for c in items[0][1:-1]]
        buttons = [set(map(int, button[1:-1].split(','))) for button in items[1:-1]]
        joltage = set(map(int, items[-1][1:-1].split(',')))
        machines.append((lights, buttons, joltage))
    return machines


def find_shortest_combo(target, buttons):
    sequences = []
    for mask in range(2 ** len(buttons)):
        bits = [c == '1' for c in ("{:0" + f"{len(buttons)}" + "b}").format(mask)]

        sequence = [buttons[i] for i, included in enumerate(bits) if included]
        sequence_state = [False] * len(target)
        for pressed in sequence:
            for wire in pressed:
                sequence_state[wire] = not sequence_state[wire]
        if sequence_state == target:
            sequences.append(sequence)

    return min(map(len, sequences))


def part_2(data):
    return 0


sample_data = read_test_input(2025, 10)
data = read_input(2025, 10)

check(part_1(sample_data), 7)
print(part_1(data))

check(part_2(sample_data), 33)
print(part_2(data))
