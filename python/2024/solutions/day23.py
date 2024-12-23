#!/usr/bin/env python3
from itertools import combinations

from utils.utils import read_input, read_test_input, check


def part_1(data):
    connections = {}
    for connection in data:
        a, b = connection.split('-')
        connections[a] = {*connections.get(a, set()), b}
        connections[b] = {*connections.get(b, set()), a}

    options = [server for server in connections.keys() if server.startswith('t')]
    networks = set()

    for option in options:
        for a, b in combinations(connections[option], 2):
            if b in connections[a]:
                network = [a, b, option]
                network.sort()
                networks.add(''.join(network))

    return len(networks)


def part_2(data):
    connections = {}
    for connection in data:
        a, b = connection.split('-')
        connections[a] = {*connections.get(a, set()), b}
        connections[b] = {*connections.get(b, set()), a}

    max_network = []
    for node in connections.keys():
        links = connections[node]
        for length in range(len(max_network), len(links) + 1):
            for potential_network in combinations(links, length):
                if all(b in connections[a] for a, b in combinations(potential_network, 2)):
                    max_network = (*potential_network, node)

    return ','.join(sorted(max_network))


sample_data = read_test_input(2024, 23)
input_data = read_input(2024, 23)

check(part_1(sample_data), 7)
print(part_1(input_data))

check(part_2(sample_data), 'co,de,ka,ta')
print(part_2(input_data))
