#!/usr/bin/env python3

from utils.utils import check, read_input, read_test_input

LEFT, RIGHT, FORWARD = 'LRF'
NORTH, EAST, SOUTH, WEST = 'NESW'


def main():
    sample_data = read_test_input(2020, 12)
    data = read_input(2020, 12)

    check(part_1(sample_data), 25)
    print(part_1(data))

    check(part_2(sample_data), 286)
    print(part_2(data))


def part_1(data):
    d = EAST
    x, y = 0, 0

    def move(direction, steps):
        nonlocal x, y
        if direction == NORTH:
            y += steps
        elif direction == SOUTH:
            y -= steps
        elif direction == EAST:
            x += steps
        elif direction == WEST:
            x -= steps

    for entry in data:
        operation = entry[0]
        steps = int(entry[1:])

        if operation == RIGHT:
            rotate = round(steps / 90)
            directions = list('NESW')
            d = directions[(directions.index(d) + rotate) % len(directions)]
        if operation == LEFT:
            rotate = round(steps / 90)
            directions = list('NESW')
            d = directions[(directions.index(d) - rotate) % len(directions)]
        elif operation == FORWARD:
            move(d, steps)
        else:
            move(operation, steps)

    return abs(x) + abs(y)


def part_2(data):
    x, y = 0, 0
    wx, wy = 10, 1

    def move(direction, steps):
        nonlocal wx, wy
        if direction == NORTH:
            wy += steps
        elif direction == SOUTH:
            wy -= steps
        elif direction == EAST:
            wx += steps
        elif direction == WEST:
            wx -= steps

    for entry in data:
        operation = entry[0]
        steps = int(entry[1:])

        if operation == RIGHT and steps == 90 or operation == LEFT and steps == 270:
            tmp = -wx
            wx = wy
            wy = tmp
        elif (operation == RIGHT or operation == LEFT) and steps == 180:
            wx = -wx
            wy = -wy
        elif operation == RIGHT and steps == 270 or operation == LEFT and steps == 90:
            tmp = wx
            wx = -wy
            wy = tmp
        elif operation == FORWARD:
            x += wx * steps
            y += wy * steps
        else:
            move(operation, steps)

    return abs(x) + abs(y)


if __name__ == '__main__':
    main()
