#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
keypad_positions = {
    '7': (0, 0),
    '8': (0, 1),
    '9': (0, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '1': (2, 0),
    '2': (2, 1),
    '3': (2, 2),
    ' ': (3, 0),
    '0': (3, 1),
    'A': (3, 2),
}

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
directional_positions = {
    ' ': (0, 0),
    '^': (0, 1),
    'A': (0, 2),
    '<': (1, 0),
    'v': (1, 1),
    '>': (1, 2),
}


def find_move_options(current_symbol, next_symbol, positions):
    position = positions[current_symbol]
    required_position = positions[next_symbol]
    row, col = position
    v_diff = required_position[0] - row
    h_diff = required_position[1] - col

    result = []

    moves_to_make = ['A']
    if v_diff < 0:
        for _ in range(abs(v_diff)):
            moves_to_make.append('^')
    elif v_diff > 0:
        for _ in range(v_diff):
            moves_to_make.append('v')
    if h_diff < 0:
        for _ in range(abs(h_diff)):
            moves_to_make.append('<')
    elif h_diff > 0:
        for _ in range(h_diff):
            moves_to_make.append('>')

    empty_position = positions[' ']
    # if start in the same row, vertical first
    if empty_position[0] == row and empty_position[1] == required_position[1]:
        moves_to_make.sort(key=lambda k: 'v^<>A'.index(k))
        result.append(''.join(moves_to_make))
    # if start in the same col, horizontal first
    elif empty_position[1] == col and empty_position[0] == required_position[0]:
        moves_to_make.sort(key=lambda k: '<>v^A'.index(k))
        result.append(''.join(moves_to_make))
    else:
        moves_to_make.sort(key=lambda k: 'v^<>A'.index(k))
        result.append(''.join(moves_to_make))
        moves_to_make.sort(key=lambda k: '<>v^A'.index(k))
        result.append(''.join(moves_to_make))

    return result


def process_sequence(sequence, depth, target_depth, cache):
    if depth > target_depth:
        return sequence

    result_sequence = ''
    for i, current_symbol in enumerate(f'A{sequence}'[: -1]):
        next_symbol = sequence[i]
        cache_key = (current_symbol, next_symbol, depth)

        if cache_key not in cache:
            positions = keypad_positions if depth == 0 else directional_positions
            move_options = find_move_options(current_symbol, next_symbol, positions)

            shortest_sequence = None
            for option in move_options:
                new_sequence = process_sequence(option, depth + 1, target_depth, cache)
                if shortest_sequence is None or len(shortest_sequence) > len(new_sequence):
                    shortest_sequence = new_sequence
            cache[cache_key] = shortest_sequence

        result_sequence = result_sequence + cache[cache_key]
    return result_sequence


def part_1(data):
    cache = {}

    answer = 0
    for code in data:
        sequence = process_sequence(code, 0, 2, cache)
        answer = answer + int(code[:-1]) * len(sequence)
    return answer


def part_2(data):
    cache = {}

    answer = 0
    for code in data:
        sequence = process_sequence(code, 0, 25, cache)
        answer = answer + int(code[:-1]) * len(sequence)
    return answer


sample_data = read_test_input(2024, 21)
input_data = read_input(2024, 21)

check(part_1(sample_data), 126384)
print(part_1(input_data))

print(part_2(input_data))
