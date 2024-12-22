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


def generate_all_sequences(seed):
    result = {}
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
            if key not in result:
                result[key] = current_price

    return result


def part_2(data):
    sellers_sequences = [generate_all_sequences(seed) for seed in map(int, data)]
    max_sell = 0
    checked = set()
    for i, seller_sequences in enumerate(sellers_sequences):
        for sequence in seller_sequences.keys():
            if sequence in checked:
                continue
            else:
                checked.add(sequence)
            sell = seller_sequences[sequence]
            for next_seller in sellers_sequences[i + 1:]:
                sell = sell + next_seller.get(sequence, 0)
            max_sell = max(sell, max_sell)
    return max_sell


sample_data = read_test_input(2024, 22)
sample_data2 = read_input(2024, 22, '_test2')
input_data = read_input(2024, 22)

check(part_1(sample_data), 37327623)
print(part_1(input_data))

check(part_2(sample_data2), 23)
print(part_2(input_data))
