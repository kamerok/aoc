#!/usr/bin/env python3
import networkx as nx
import gravis as gv

from utils.utils import read_input, read_test_input, check


def generate_graph(edges):
    g = nx.DiGraph()
    g.add_edges_from(edges)
    fig = gv.d3(g)
    fig.export_html('graph.html')


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
    # this one is a mess
    # with graph visualisation I found a set of variables (node) that derives certain z bit
    # that it was a matter of trying different combinations to fix the node
    swaps = (
        ('hkh', 'z31'),
        ('z27', 'bfq'),
        ('hmt', 'z18'),
        ('bng', 'fjp'),
    )

    swaps_map = {}
    for a, b in swaps:
        swaps_map[a] = b
        swaps_map[b] = a

    original_values = {}
    gates = {}
    effects = {}
    for line in data:
        if ':' in line:
            key, value = line.split(': ')
            original_values[key] = bool(int(value))
        elif '->' in line:
            a, operation, b, _, target = line.split()
            if target in swaps_map:
                target = swaps_map[target]
            gates[target] = (operation, a, b)
            effects[a] = {*effects.get(a, set()), target}
            effects[b] = {*effects.get(b, set()), target}

    values = dict(original_values)

    x = get_binary_number('x', values)
    y = get_binary_number('y', values)
    z = evaluate_z(values, gates)

    expected = f'{(int(x, 2) + int(y, 2)):b}'
    print(expected)
    print(z)

    values = dict(original_values)

    for i in range(45):
        values[f'x{i:02d}'] = True
        values[f'y{i:02d}'] = True

    x = get_binary_number('x', values)
    y = get_binary_number('y', values)
    z = evaluate_z(values, gates)

    expected = f'{(int(x, 2) + int(y, 2)):b}'
    print(expected)
    print(z)

    for i in range(len(expected)):
        z_bit = z[len(z) - 1 - i]
        expected_bit = expected[len(expected) - 1 - i]
        if z_bit != expected_bit:
            print(f'z{i}', expected_bit, z_bit)

    values = dict(original_values)

    for i in range(45):
        values[f'x{i:02d}'] = i % 2 > 0
        values[f'y{i:02d}'] = i % 2 == 0

    x = get_binary_number('x', values)
    y = get_binary_number('y', values)
    z = evaluate_z(values, gates)

    expected = f'{(int(x, 2) + int(y, 2)):b}'
    print(expected)
    print(z)

    for i in range(len(expected)):
        z_bit = z[len(z) - 1 - i]
        expected_bit = expected[len(expected) - 1 - i]
        if z_bit != expected_bit:
            print(f'z{i}', expected_bit, z_bit)

    edges = []
    for key, value in effects.items():
        for v in value:
            edges.append((key + f'[{values[key]}]', v+f'[{values[v]}]'))
    generate_graph(edges)

    return print(','.join(sorted(swaps_map.keys())))


sample_data = read_test_input(2024, 24)
sample_data2 = read_input(2024, 24, '_test2')
input_data = read_input(2024, 24)

check(part_1(sample_data), 2024)
print(part_1(input_data))
assert part_1(input_data) == 51745744348272

print(part_2(input_data))
