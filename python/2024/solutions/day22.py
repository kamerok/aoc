#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def mix(a, b):
    return a ^ b


def prune(n):
    return n % 16777216


def evolve(n):
    n = prune(mix(n, n * 64))
    n = prune(mix(n, int(n / 32)))
    n = prune(mix(n, n * 2048))
    return n


def evolve_multiple(n, times):
    for _ in range(times):
        n = evolve(n)
    return n


def part_1(data):
    return sum(evolve_multiple(n, 2000) for n in map(int, data))


def generate_all_sequences(seed, all_sequences):
    keys = set()
    current_price = seed % 10
    window = []
    for _ in range(2000):
        seed = evolve(seed)
        new_price = seed % 10
        window.append(new_price - current_price)
        current_price = new_price
        if len(window) > 4:
            window.pop(0)
        if len(window) == 4:
            key = tuple(window)
            if key not in keys:
                keys.add(key)
                all_sequences[key] = all_sequences.get(key, 0) + current_price


def part_2(data):
    sequences = {}
    for seed in map(int, data):
        generate_all_sequences(seed, sequences)
    return max(sequences.values())


sample_data = read_test_input(2024, 22)
sample_data2 = read_input(2024, 22, '_test2')
input_data = read_input(2024, 22)

check(part_1(sample_data), 37327623)
print(part_1(input_data))

check(part_2(sample_data2), 23)
print(part_2(input_data))
