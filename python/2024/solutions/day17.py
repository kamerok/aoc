#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check, a_star_path


def execute_program(a, commands):
    b = 0
    c = 0
    output = []
    i = 0
    while 0 <= i < len(commands):
        opcode = commands[i]
        literal = commands[i + 1]

        def combo_operand():
            match literal:
                case 4:
                    return a
                case 5:
                    return b
                case 6:
                    return c
                case 7:
                    raise Exception('Combo operand 7 is reserved and will not appear in valid programs')
                case _:
                    return literal

        match opcode:
            case 0:
                a = int(a / pow(2, combo_operand()))
            case 1:
                b = b ^ literal
            case 2:
                b = combo_operand() % 8
            case 3:
                if a != 0:
                    i = literal - 2  # compensate increase
            case 4:
                b = b ^ c
            case 5:
                output.append(combo_operand() % 8)
            case 6:
                b = int(a / pow(2, combo_operand()))
            case 7:
                c = int(a / pow(2, combo_operand()))
        i = i + 2
    return output


def part_1(data):
    a = int(data[0][12:])
    commands = list(map(int, data[4][9:].split(',')))
    return ','.join(map(str, execute_program(a, commands)))


def part_2(data):
    commands_raw = data[4][9:]
    commands = list(map(int, commands_raw.split(',')))

    to_check = [(len(commands) - 1, 0)]
    while to_check:
        index, current_sum = to_check.pop(0)
        for i in range(8):
            current_3_bits = pow(2, index * 3) * i
            local_sum = current_sum + current_3_bits
            local_result = execute_program(local_sum, commands)
            if len(local_result) == len(commands) and local_result[index] == commands[index]:
                if index == 0:
                    return local_sum
                to_check.append((index - 1, local_sum))


sample_data = read_test_input(2024, 17)
sample_data2 = read_input(2024, 17, suffix='_test2')
input_data = read_input(2024, 17)

check(part_1(sample_data), "4,6,3,5,6,3,5,2,1,0")
print(part_1(input_data))

check(part_2(sample_data2), 117440)
print(part_2(input_data))
