#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def part_1(data):
    shapes, slots = parse_input(data)
    answer = 0
    for area, counts in slots:
        min_space = sum(c * shapes[i] for i, c in enumerate(counts))
        full_area = area[0] * area[1]
        if min_space / full_area <= .85:
            answer += 1
    return answer


def parse_input(data):
    shapes = []
    slots = []
    blocks = ('\n'.join(data)).split('\n\n')
    for block in blocks[:-1]:
        shapes.append(sum(1 for c in block if c == '#'))
    for slot in blocks[-1].split('\n'):
        raw_area, raw_counts = slot.split(': ')
        slots.append((tuple(map(int, raw_area.split('x'))), list(map(int, raw_counts.split()))))
    return shapes, slots


sample_data = read_test_input(2025, 12)
data = read_input(2025, 12)

check(part_1(sample_data), 2)
print(part_1(data))
