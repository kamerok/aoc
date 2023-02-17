#!/usr/bin/env python3

from utils.utils import check, read_input, read_test_input


def main():
    sample_data = read_test_input(2020, 13)
    data = read_input(2020, 13)

    check(part_1(sample_data), 295)
    print(part_1(data))

    check(part_2(sample_data[1]), 1068781)
    check(part_2('17,x,13,19'), 3417)
    check(part_2('67,7,59,61'), 754018)
    check(part_2('67,x,7,59,61'), 779210)
    check(part_2('67,7,x,59,61'), 1261476)
    check(part_2('1789,37,47,1889'), 1202161486)
    print(part_2(data[1]))


def part_1(data):
    depart = int(data[0])
    busses = list(map(int, filter(lambda x: x != 'x', data[1].split(','))))
    closest_bus = busses[0]
    arrive_in = busses[0]
    for bus in busses:
        new_arrive = bus - depart % bus
        if new_arrive < arrive_in:
            closest_bus = bus
            arrive_in = new_arrive
    return closest_bus * arrive_in


def part_2(data):
    busses = {}
    for i, bus in enumerate(data.split(',')):
        if bus != 'x':
            bus = int(bus)
            busses[bus] = i

    def check_number(n):
        return all(map(lambda bus: (n + busses[bus]) % bus == 0, list(busses.keys())))

    keys = list(busses.keys())
    index_to_align = 1
    advance = keys[0]
    number = 0
    while not check_number(number):
        number += advance
        bus_to_align = keys[index_to_align]
        if (number + busses[bus_to_align]) % bus_to_align == 0:
            index_to_align += 1
            advance *= bus_to_align

    return number


if __name__ == '__main__':
    main()
