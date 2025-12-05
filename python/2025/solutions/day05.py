#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def part_1(data):
    ids, ranges = parse_data(data)
    return sum(any(id in range for range in ranges) for id in ids)


def parse_data(data):
    raw_ranges, raw_ids = map(lambda block: block.split('\n'), '\n'.join(data).split('\n\n'))
    ranges = [range(int(start), int(end) + 1) for start, end in map(lambda raw_range: raw_range.split('-'), raw_ranges)]
    ids = [int(raw_id) for raw_id in raw_ids]
    return ids, ranges


def part_2(data):
    _, ranges = parse_data(data)
    borders_to_ranges = []
    for r in set(ranges):
        borders_to_ranges.append((r.start, r))
        borders_to_ranges.append((r.stop, r))
    borders_to_ranges.sort(key=lambda item: item[0])

    result_ranges = []
    current_start = None
    open_ranges = set()
    for border, r in borders_to_ranges:
        if border == r.start:
            if current_start is None:
                current_start = border
            open_ranges.add(r)
        else:
            open_ranges.remove(r)
            if len(open_ranges) == 0:
                result_ranges.append(range(current_start, border))
                current_start = None

    return sum(len(r) for r in result_ranges)


sample_data = read_test_input(2025, 5)
data = read_input(2025, 5)

check(part_1(sample_data), 3)
print(part_1(data))

check(part_2(sample_data), 14)
print(part_2(data))
