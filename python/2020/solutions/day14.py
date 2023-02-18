#!/usr/bin/env python3
import re

from utils.utils import check, read_input, read_test_input

rexp = re.compile(r'mem\[(\d+)\] = (\d+)')


def main():
    sample_data = read_test_input(2020, 14)
    sample_data_2 = read_input(2020, 14, '_test2')
    data = read_input(2020, 14)

    check(part_1(sample_data), 165)
    print(part_1(data))

    check(part_2(sample_data_2), 208)
    print(part_2(data))


def part_1(data):
    register = {}
    for entry in data:
        if entry.startswith('mask'):
            mask = entry.split(' = ')[1]
        else:
            i, n = map(int, rexp.findall(entry)[0])
            binary = '{0:036b}'.format(n)
            bits = []
            for mask_bit, number_bit in zip(mask, binary):
                if mask_bit != 'X':
                    bits.append(mask_bit)
                else:
                    bits.append(number_bit)
            register[i] = int(''.join(bits), 2)

    return sum(register.values())


def part_2(data):
    register = {}
    for entry in data:
        if entry.startswith('mask'):
            mask = entry.split(' = ')[1]
        else:
            i, n = map(int, rexp.findall(entry)[0])
            binary = '{0:036b}'.format(i)
            addresses = [[]]
            for mask_bit, address_bit in zip(mask, binary):
                if mask_bit == '0':
                    for address in addresses:
                        address.append(address_bit)
                elif mask_bit == '1':
                    for address in addresses:
                        address.append('1')
                if mask_bit == 'X':
                    new_addresses = []
                    for address in addresses:
                        new_address = address.copy()
                        new_address.append('0')
                        new_addresses.append(new_address)
                        address.append('1')
                    for new_address in new_addresses:
                        addresses.append(new_address)

            for address in addresses:
                i = int(''.join(address), 2)
                register[i] = n

    return sum(register.values())


if __name__ == '__main__':
    main()
