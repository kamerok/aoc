#!/usr/bin/env python3
import re

from utils.utils import read_input, read_test_input, check


def part_1(data):
    chunks = "\n".join(data).split("\n\n")
    seeds = list(map(int, re.findall(r"\d+", chunks[0])))
    mappings = list(
        map(lambda chunk: list(map(lambda line: list(map(int, line.split())), chunk.split('\n')[1:])), chunks[1:])
    )

    def transform_seed(seed):
        for mapping in mappings:
            matching_rules = [rule for rule in mapping if rule[1] <= seed < rule[1] + rule[2]]
            if len(matching_rules) == 1:
                rule = matching_rules[0]
                seed = seed + rule[0] - rule[1]
        return seed

    return min(map(transform_seed, seeds))


def split_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


def part_2(data):
    chunks = "\n".join(data).split("\n\n")
    seed_ranges = split_list(list(map(int, re.findall(r"\d+", chunks[0]))), 2)
    seed_ranges = list(map(lambda r: [r[0], r[0] + r[1]], seed_ranges))
    mappings = list(
        map(lambda chunk: list(map(lambda line: list(map(int, line.split())), chunk.split('\n')[1:])), chunks[1:])
    )

    def split_range_by_transformation(r, transformation):
        t_start = transformation[1]
        t_end = transformation[1] + transformation[2]
        if not (t_start <= r[0] < t_end or t_start <= r[1] < t_end):
            return [r]
        if t_start <= r[0] and r[1] <= t_end:
            return [[r[0], r[1]]]
        elif r[0] < t_start < r[1] and r[0] < t_end < r[1]:
            return [[r[0], t_start], [t_start, t_end], [t_end, r[1]]]
        elif t_start <= r[0]:
            return [[r[0], t_end], [t_end, r[1]]]
        else:
            return [[r[0], t_start], [t_start, r[1]]]

    def apply_transformation(r, transformation):
        diff = transformation[0] - transformation[1]
        t_start = transformation[1]
        t_end = transformation[1] + transformation[2]
        if not (t_start <= r[0] < t_end or t_start <= r[1] < t_end):
            return [r]
        if t_start <= r[0] and r[1] <= t_end:
            return [[r[0] + diff, r[1] + diff]]
        elif r[0] < t_start < r[1] and r[0] < t_end < r[1]:
            return [[r[0], t_start], [t_start + diff, t_end + diff], [t_end + diff, r[1]]]
        elif t_start <= r[0]:
            return [[r[0] + diff, t_end + diff], [t_end, r[1]]]
        else:
            return [[r[0], t_start], [t_start + diff, r[1] + diff]]

    def transform_ranges(ranges, transformations):
        result = []

        for t in transformations:
            ranges = [r for ranges in map(lambda r: split_range_by_transformation(r, t), ranges) for r in ranges]
        for r in ranges:
            matched_transformations = [t for t in transformations if
                                       t[1] <= r[0] < t[1] + t[2] or t[1] <= r[1] < t[1] + t[2]]
            if len(matched_transformations) == 0:
                result.append(r)
            for matched_transformation in matched_transformations:
                transformed = apply_transformation(r, matched_transformation)
                result.extend(transformed)
        return result

    def transform_range(seed_range):
        ranges = [seed_range]
        for mapping in mappings:
            ranges = transform_ranges(ranges, mapping)
        return ranges

    final_ranges = [r for ranges in list(map(transform_range, seed_ranges)) for r in ranges]
    return min(map(min, final_ranges))


sample_data = read_test_input(2023, 5)
data = read_input(2023, 5)

check(part_1(sample_data), 35)
print(part_1(data))

check(part_2(sample_data), 46)
print(part_2(data))
