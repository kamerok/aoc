#!/usr/bin/env python3
from utils.utils import read_input, read_test_input, check


def part_1(data):
    data = list(map(int, data))
    total_length = sum(data)
    answer = 0
    unwrapped_index = 0
    front_file_index = 0

    end_value_unwrapped_index = total_length - 1

    end_value_index = int(len(data) / 2)
    end_value_length_index = int(len(data) - 1)
    end_value_length_left = data[end_value_length_index]
    for i in range(0, len(data)):
        if i % 2 == 0:
            # file
            file_length = data[i]
            for _ in range(0, file_length):
                if unwrapped_index > end_value_unwrapped_index:
                    return answer

                answer = answer + unwrapped_index * front_file_index
                unwrapped_index = unwrapped_index + 1
            front_file_index = front_file_index + 1
        else:
            # space
            space_length = data[i]
            for _ in range(0, space_length):
                if unwrapped_index > end_value_unwrapped_index:
                    return answer

                answer = answer + unwrapped_index * end_value_index
                end_value_length_left = end_value_length_left - 1
                if end_value_length_left == 0:
                    end_value_index = end_value_index - 1
                    end_value_unwrapped_index = end_value_unwrapped_index - data[end_value_length_index - 1]
                    end_value_length_index = end_value_length_index - 2
                    end_value_length_left = data[end_value_length_index]
                unwrapped_index = unwrapped_index + 1
                end_value_unwrapped_index = end_value_unwrapped_index - 1
    return 0


def part_2(data):
    data = list(map(int, data))

    model = []  # (index, length)
    for i in range(0, len(data)):
        if i % 2 == 0:
            # file
            file_length = data[i]
            model.append((int(i / 2), file_length))
        else:
            # space
            space_length = data[i]
            model.append((None, space_length))

    process_queue = []
    for index, length in reversed(model):
        if index is not None:
            process_queue.append((index, length))

    while len(process_queue) > 0:
        file_to_move = process_queue.pop(0)
        _, file_length = file_to_move
        file_index = model.index(file_to_move)
        for i in range(file_index):
            index, length = model[i]
            if index is None and length >= file_length:
                # move
                model[file_index] = (None, file_length)
                model[i] = file_to_move
                if file_length < length:
                    model.insert(i + 1, (None, length - file_length))
                break

    unwrapped_index = 0
    answer = 0
    for index, length in model:
        for _ in range(length):
            answer = answer + unwrapped_index * (index or 0)
            unwrapped_index = unwrapped_index + 1
    return answer


sample_data = read_test_input(2024, 9)[0]
data = read_input(2024, 9)[0]

check(part_1(sample_data), 1928)
print(part_1(data))

check(part_2(sample_data), 2858)
print(part_2(data))
