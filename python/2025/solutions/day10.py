#!/usr/bin/env python3
from scipy.optimize import linprog

from utils.utils import read_input, read_test_input, check


def part_1(data):
    machines = parse_input(data)
    return sum(find_shortest_light(target, buttons) for target, buttons, _ in machines)


def parse_input(data):
    machines = []
    for line in data:
        items = line.split(' ')
        lights = [1 if c == '#' else 0 for c in items[0][1:-1]]
        buttons = [set(map(int, button[1:-1].split(','))) for button in items[1:-1]]
        joltage = list(map(int, items[-1][1:-1].split(',')))
        machines.append((lights, buttons, joltage))
    return machines


def find_shortest_light(target, buttons):
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
    machines = parse_input(data)
    return sum(find_shortest_joltage(target, buttons) for _, buttons, target in machines)


def find_shortest_joltage(target, buttons):
    A = [[1 if i in button else 0 for button in buttons] for i in range(len(target))]
    b = target
    solution = linprog(c=[1] * len(A[0]),
                       A_eq=A,
                       b_eq=b,
                       integrality=[1] * len(A[0]))
    return sum(solution['x'])


sample_data = read_test_input(2025, 10)
data = read_input(2025, 10)

check(part_1(sample_data), 7)
print(part_1(data))

check(part_2(sample_data), 33)
print(part_2(data))
