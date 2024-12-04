#!/usr/bin/env python3

from utils.utils import read_input, read_test_input, check


def part_1(data):
    xmas_mapping = {
        'X': 'M',
        'M': 'A',
        'A': 'S'
    }

    def check_word(grid, letter, row, col, d_row, d_col) -> bool:
        if not 0 <= row < len(grid) or not 0 <= col < len(grid[0]):
            return False
        if letter != grid[row][col]:
            return False
        if letter == 'S':
            return True

        return check_word(grid, xmas_mapping[letter], row + d_row, col + d_col, d_row, d_col)

    answer = 0
    for row in range(0, len(data)):
        for col in range(0, len(data[0])):
            if data[row][col] == 'X':
                answer = answer + sum((
                    check_word(data, 'X', row, col, -1, -1),
                    check_word(data, 'X', row, col, -1, 0),
                    check_word(data, 'X', row, col, -1, 1),
                    check_word(data, 'X', row, col, 0, 1),
                    check_word(data, 'X', row, col, 1, 1),
                    check_word(data, 'X', row, col, 1, 0),
                    check_word(data, 'X', row, col, 1, -1),
                    check_word(data, 'X', row, col, 0, -1),
                ))
    return answer


def part_2(data):
    # MMSS
    x_mas_options = (
        ((1, -1), (-1, -1), (-1, 1), (1, 1)),
        ((-1, -1), (-1, 1), (1, -1), (1, 1)),
        ((-1, 1), (1, 1), (-1, -1), (1, -1)),
        ((1, -1), (1, 1), (-1, -1), (-1, 1)),
    )

    def check_option(grid, row, col, option):
        return all((
            grid[row + option[0][0]][col + option[0][1]] == 'M',
            grid[row + option[1][0]][col + option[1][1]] == 'M',
            grid[row + option[2][0]][col + option[2][1]] == 'S',
            grid[row + option[3][0]][col + option[3][1]] == 'S',
        ))

    def check_pattern(grid, row, col):
        return any(map(lambda option: check_option(grid, row, col, option), x_mas_options))

    answer = 0
    for row in range(1, len(data) - 1):
        for col in range(1, len(data[0]) - 1):
            if data[row][col] == 'A':
                answer = answer + check_pattern(data, row, col)
    return answer


sample_data = read_test_input(2024, 4)
data = read_input(2024, 4)

check(part_1(sample_data), 18)
print(part_1(data))

check(part_2(sample_data), 9)
print(part_2(data))
