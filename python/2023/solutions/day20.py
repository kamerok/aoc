#!/usr/bin/env python3
from enum import Enum

from utils.utils import read_input, check, read_test_input


class Module(Enum):
    FLIP_FLOP = 1
    CONJUNCTION = 2
    BROADCAST = 3


def parse_modules(data):
    modules = {}
    for line in data:
        from_raw, to_raw = line.split(' -> ')
        type = Module.BROADCAST
        name = from_raw
        if from_raw[0] == '%':
            type = Module.FLIP_FLOP
            name = from_raw[1:]
        elif from_raw[0] == '&':
            type = Module.CONJUNCTION
            name = from_raw[1:]
        modules[name] = {
            'type': type,
            'destinations': to_raw.split(', ')
        }
    return modules


def process_button_press(conjunction_memory, enabled_flip_flops, modules):
    low_sent, high_sent = 0, 0
    to_process = [('', 'broadcaster', 0)]
    while len(to_process) > 0:
        pulse_source, module_name, pulse = to_process.pop(0)
        if pulse == 1:
            high_sent = high_sent + 1
        else:
            low_sent = low_sent + 1
        if module_name not in modules:
            continue
        module = modules[module_name]
        if module['type'] == Module.FLIP_FLOP and pulse == 0:
            if module_name in enabled_flip_flops:
                enabled_flip_flops.remove(module_name)
                to_process.extend(map(lambda module: (module_name, module, 0), module['destinations']))
            else:
                enabled_flip_flops.append(module_name)
                to_process.extend(map(lambda module: (module_name, module, 1), module['destinations']))
        elif module['type'] == Module.CONJUNCTION:
            conjunction_memory[module_name][pulse_source] = pulse
            is_all_high = all(v == 1 for v in conjunction_memory[module_name].values())
            new_pulse = 0 if is_all_high else 1
            to_process.extend(map(lambda module: (module_name, module, new_pulse), module['destinations']))
        elif module['type'] == Module.BROADCAST:
            to_process.extend(map(lambda module: (module_name, module, 0), module['destinations']))
    return high_sent, low_sent


def part_1(data):
    modules = parse_modules(data)

    enabled_flip_flops = []
    conjunction_memory = {}

    conjunctions = list(filter(lambda key: modules[key]['type'] == Module.CONJUNCTION, modules.keys()))
    for conjunction_name in conjunctions:
        inputs = list(filter(lambda key: conjunction_name in modules[key]['destinations'], modules.keys()))
        conjunction_memory[conjunction_name] = {i: 0 for i in inputs}

    high_sent, low_sent = 0, 0

    for _ in range(1000):
        press_high_sent, press_low_sent = process_button_press(conjunction_memory, enabled_flip_flops, modules)
        high_sent = high_sent + press_high_sent
        low_sent = low_sent + press_low_sent

    return low_sent * high_sent


def is_pulse_for_module_received(target_module, conjunction_memory, enabled_flip_flops, modules):
    to_process = [('', 'broadcaster', 0)]
    while len(to_process) > 0:
        pulse_source, module_name, pulse = to_process.pop(0)
        if pulse_source == target_module and pulse == 1:
            return True
        if module_name not in modules:
            continue
        module = modules[module_name]
        if module['type'] == Module.FLIP_FLOP and pulse == 0:
            if module_name in enabled_flip_flops:
                enabled_flip_flops.remove(module_name)
                to_process.extend(map(lambda module: (module_name, module, 0), module['destinations']))
            else:
                enabled_flip_flops.append(module_name)
                to_process.extend(map(lambda module: (module_name, module, 1), module['destinations']))
        elif module['type'] == Module.CONJUNCTION:
            conjunction_memory[module_name][pulse_source] = pulse
            is_all_high = all(v == 1 for v in conjunction_memory[module_name].values())
            new_pulse = 0 if is_all_high else 1
            to_process.extend(map(lambda module: (module_name, module, new_pulse), module['destinations']))
        elif module['type'] == Module.BROADCAST:
            to_process.extend(map(lambda module: (module_name, module, 0), module['destinations']))
    return False


def pulse_for_module_received_presses(target_module, conjunction_memory, enabled_flip_flops, modules):
    presses = 1

    while not is_pulse_for_module_received(target_module, conjunction_memory, enabled_flip_flops, modules):
        presses = presses + 1

    return presses


def part_2(data):
    modules = parse_modules(data)

    to_check = ('pm', 'mk', 'pk', 'hf')

    result = 1

    for module in to_check:
        enabled_flip_flops = []
        conjunction_memory = {}

        conjunctions = list(filter(lambda key: modules[key]['type'] == Module.CONJUNCTION, modules.keys()))
        for conjunction_name in conjunctions:
            inputs = list(filter(lambda key: conjunction_name in modules[key]['destinations'], modules.keys()))
            conjunction_memory[conjunction_name] = {i: 0 for i in inputs}

        result = result * pulse_for_module_received_presses(module, conjunction_memory, enabled_flip_flops, modules)

    return result


sample_data = read_test_input(2023, 20)
sample_data2 = read_input(2023, 20, '_test2')
data = read_input(2023, 20)

check(part_1(sample_data), 32000000)
check(part_1(sample_data2), 11687500)
print(part_1(data))

print(part_2(data))
