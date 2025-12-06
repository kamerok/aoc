#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def part_1(data):
    return sum_numbers(parse_part_1(data))


def sum_numbers(data):
    answer = 0
    for problem in data:
        operator = problem[-1]
        local_answer = 1 if operator == '*' else 0
        for item in problem[:-1]:
            if operator == '*':
                local_answer *= item
            else:
                local_answer += item
        answer += local_answer
    return answer


def parse_part_1(data):
    parsed = [tuple(map(lambda item: int(item) if item not in '*+' else item, line.split())) for line in data]
    return transposed(parsed)


def transposed(iterable):
    return list(zip(*iterable))


def parse_part_2(data):
    block_starts = [i for i, c in enumerate(data[-1]) if c in '*+']
    block_starts.append(max(map(len, data)) + 1)
    problems = []
    for block_index, block_start in enumerate(block_starts[:-1]):
        sign = data[-1][block_start]
        block = []
        for col in range(block_start, block_starts[block_index + 1] - 1):
            line = []
            for row in range(0, len(data) - 1):
                if col >= len(data[row]):
                    line.append(' ')
                else:
                    line.append(data[row][col])
            block.append(line)
        problem = list(map(lambda number: int(''.join(number)), block))
        problem.append(sign)
        problems.append(problem)
    return problems


def part_2(data):
    return sum_numbers(parse_part_2(data))


sample_data = read_test_input(2025, 6)
data = read_input(2025, 6)

check(part_1(sample_data), 4277556)
print(part_1(data))

check(part_2(sample_data), 3263827)
print(part_2(data))
