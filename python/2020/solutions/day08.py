#!/usr/bin/env python3

from utils.utils import check, read_test_input, read_input


def main():
    sample_data = read_test_input(2020, 8)
    data = read_input(2020, 8)

    check(part_1(sample_data), 5)
    print(part_1(data))

    check(part_2(sample_data), 8)
    print(part_2(data))


def part_1(data):
    return execute(data)[1]


def part_2(data):
    possible_update_indexes = list(filter(lambda i: data[i].startswith(('nop', 'jmp')), range(len(data))))

    for i in possible_update_indexes:
        command, number = data[i].split()
        new_data = list(data)
        if command == 'nop':
            new_command = 'jmp'
        else:
            new_command = 'nop'
        new_data[i] = f'{new_command} {number}'
        is_infinite, state = execute(new_data)
        if not is_infinite:
            return state

    return None


def execute(data):
    executed = set()
    index = 0
    state = 0

    while index not in executed and index < len(data):
        executed.add(index)
        command = data[index]
        number = int(command.split()[1])
        if command.startswith('nop'):
            index += 1
        elif command.startswith('acc'):
            state += number
            index += 1
        else:
            index += number

    is_infinite = index != len(data)

    return is_infinite, state


if __name__ == '__main__':
    main()
