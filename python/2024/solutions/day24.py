#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def get_binary_number(name, values):
    number_values = {k for k in values.keys() if k.startswith(name)}
    max_index = max(int(v[1:]) for v in number_values)
    bites = [False for _ in range(max_index + 1)]
    for value in number_values:
        index = int(value[1:])
        bites[index] = values[value]
    bit_array = list(map(str, map(int, bites)))
    binary_value = ''.join(reversed(bit_array))
    return binary_value


def evaluate_z(values, gates):
    z_values = {k for k in gates.keys() if k.startswith('z')}
    to_evaluate = list(z_values)
    while to_evaluate:
        value_to_evaluate = to_evaluate[-1]
        if value_to_evaluate in values:
            to_evaluate.pop()
        else:
            operation, a, b = gates[value_to_evaluate]
            if a not in values:
                to_evaluate.append(a)
                continue
            if b not in values:
                to_evaluate.append(b)
                continue
            if operation == 'OR':
                values[value_to_evaluate] = values[a] or values[b]
            elif operation == 'AND':
                values[value_to_evaluate] = values[a] and values[b]
            else:
                values[value_to_evaluate] = values[a] ^ values[b]
            to_evaluate.pop()

    return get_binary_number('z', values)


def part_1(data):
    values = {}
    gates = {}
    for line in data:
        if ':' in line:
            key, value = line.split(': ')
            values[key] = bool(int(value))
        elif '->' in line:
            a, operation, b, _, result = line.split()
            gates[result] = (operation, a, b)

    binary_z = evaluate_z(values, gates)

    return int(binary_z, 2)


def part_2(data):
    return 0


sample_data = read_test_input(2024, 24)
sample_data2 = read_input(2024, 24, '_test2')
input_data = read_input(2024, 24)

check(part_1(sample_data), 2024)
print(part_1(input_data))
assert part_1(input_data) == 51745744348272

check(part_2(sample_data2), 'z00,z01,z02,z05')
print(part_2(input_data))
