#!/usr/bin/env python3

from utils.utils import read_input, check


def hash(line):
    current_value = 0
    for c in line:
        current_value = current_value + ord(c)
        current_value = current_value * 17
        current_value = current_value % 256
    return current_value


def part_1(data):
    return sum(map(hash, data.split(',')))


def part_2(data):
    boxes = []
    for _ in range(256):
        boxes.append([])
    for lens_string in data.split(','):
        if lens_string[-1] != '-':
            label, focus = lens_string.split('=')
            box = boxes[hash(label)]
            lens = (label, int(focus))
            existing_index = next((i for i, e in enumerate(box) if e[0] == label), None)
            if existing_index is not None:
                box[existing_index] = lens
            else:
                box.append(lens)
        else:
            label = lens_string[:-1]
            box = boxes[hash(label)]
            for lens in filter(lambda lens: lens[0] == label, box):
                box.remove(lens)

    result = 0
    for box_index, box in enumerate(boxes):
        for lens_index, lens in enumerate(box):
            result = result + (box_index + 1) * (lens_index + 1) * lens[1]
    return result


data = read_input(2023, 15)

check(part_1('HASH'), 52)
check(part_1('rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'), 1320)
print(part_1(data[0]))

check(part_2('rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'), 145)
print(part_2(data[0]))
