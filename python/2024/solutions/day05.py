#!/usr/bin/env python3
from functools import cmp_to_key

from utils.utils import read_input, read_test_input, check


def part_1(data):
    pages, rules = parse_input(data)

    correct_pages = [page for page in pages if is_correct_page(rules, page)]
    return sum(map(lambda page: page[int(len(page) / 2)], correct_pages))


def part_2(data):
    pages, rules = parse_input(data)

    incorrect_pages = [page for page in pages if not is_correct_page(rules, page)]
    corrected_pages = [correct_page(rules, page) for page in incorrect_pages]
    return sum(map(lambda page: page[int(len(page) / 2)], corrected_pages))


def parse_input(data):
    rules_raw, pages_raw = "\n".join(data).split("\n\n")
    rules = {}
    for before, after in map(lambda entry: map(int, entry.split('|')), rules_raw.split()):
        after_set = rules.get(before, set())
        after_set.add(after)
        rules[before] = after_set
    pages = list(map(lambda page: list(map(int, page.split(','))), pages_raw.split()))
    return pages, rules


def is_correct_page(rules, page):
    restricted = set()
    for item in reversed(page):
        if item in restricted:
            return False
        if item in rules:
            restricted.update(rules[item])
    return True


def correct_page(rules, page):
    def compare(x, y):
        if y in rules.get(x, set()):
            return -1
        else:
            return 0

    new_page = sorted(page, key=cmp_to_key(compare))
    return new_page


sample_data = read_test_input(2024, 5)
data = read_input(2024, 5)

check(part_1(sample_data), 143)
print(part_1(data))

check(part_2(sample_data), 123)
assert part_2(data) != 4707
print(part_2(data))
