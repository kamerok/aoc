#!/usr/bin/env python3
import math

from utils.utils import read_input, read_test_input, check


def part_1(data, n):
    points = [(x, y, z) for x, y, z in map(lambda line: map(int, line.split(',')), data)]
    connections = sort_connections(points)[:n]

    circuits = []
    for (start, end) in connections:
        start_circuit = {start}
        end_circuit = {end}
        for circuit in circuits:
            if start in circuit:
                start_circuit = circuit
            if end in circuit:
                end_circuit = circuit
        if start_circuit in circuits:
            circuits.remove(start_circuit)
        if end_circuit in circuits:
            circuits.remove(end_circuit)
        circuits.append(start_circuit.union(end_circuit))

    circuits.sort(key=len)
    circuits.reverse()
    return math.prod(map(len, circuits[:3]))


def sort_connections(points):
    distances = []
    for i, start in enumerate(points):
        for end in points[i + 1:]:
            distances.append(({start, end}, distance(start, end)))
    distances.sort(key=lambda item: item[1])
    return list(map(lambda d: d[0], distances))


def distance(start, end):
    return math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2 + (end[2] - start[2]) ** 2)


def part_2(data):
    points = [(x, y, z) for x, y, z in map(lambda line: map(int, line.split(',')), data)]
    connections = sort_connections(points)

    processed_point = set()
    circuits = []
    for (start, end) in connections:
        start_circuit = {start}
        end_circuit = {end}
        for circuit in circuits:
            if start in circuit:
                start_circuit = circuit
            if end in circuit:
                end_circuit = circuit
        if start_circuit in circuits:
            circuits.remove(start_circuit)
        if end_circuit in circuits:
            circuits.remove(end_circuit)
        circuits.append(start_circuit.union(end_circuit))
        processed_point.add(start)
        processed_point.add(end)
        if len(processed_point) == len(points):
            return start[0] * end[0]
    return 0


sample_data = read_test_input(2025, 8)
data = read_input(2025, 8)

check(part_1(sample_data, 10), 40)
print(part_1(data, 1000))

check(part_2(sample_data), 25272)
print(part_2(data))
