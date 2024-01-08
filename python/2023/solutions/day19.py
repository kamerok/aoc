#!/usr/bin/env python3

from utils.utils import read_input, check, read_test_input


def parse_rules(data):
    raw_rules = '\n'.join(data).split('\n\n')[0]

    def parse_rule(raw_rule):
        name, rule = raw_rule[:-1].split('{')
        return name, rule.split(',')

    rules = {k: v for k, v in map(parse_rule, raw_rules.split())}

    return rules


def part_1(data):
    raw_parts = '\n'.join(data).split('\n\n')[1]

    def parse_part(raw_part):
        part = {k: int(v) for k, v in map(lambda pair: pair.split('='), raw_part[1:-1].split(','))}
        return part

    parts = [parse_part(raw_part) for raw_part in raw_parts.split()]

    rules = parse_rules(data)

    accepted = filter(lambda part: is_part_accepted(part, rules), parts)

    return sum(map(lambda part: sum(part.values()), accepted))


def is_part_accepted(part, rules):
    current_rule_name = 'in'
    while current_rule_name not in ('A', 'R'):
        checks = list(rules[current_rule_name])

        def is_applicable(check):
            if ':' not in check:
                return True
            param = check[0]
            sign = check[1]
            value = int(check[2:].split(':')[0])
            if sign == '>':
                return part[param] > value
            else:
                return part[param] < value

        applicable_check = next(filter(is_applicable, checks))

        if ':' not in applicable_check:
            current_rule_name = applicable_check
        else:
            current_rule_name = applicable_check.split(':')[1]

    if current_rule_name == 'A':
        return True
    else:
        return False


def part_2(data):
    rules = parse_rules(data)
    accepted_part_range = {'x': range(1, 4001), 'm': range(1, 4001), 'a': range(1, 4001), 's': range(1, 4001)}

    accepted_ranges = []

    def process_range_with_rule(accepted_part_range, rule_name):
        if rule_name == 'A':
            accepted_ranges.append(accepted_part_range)
            return
        if rule_name == 'R':
            return

        checks = list(rules[rule_name])

        current_part_range = accepted_part_range
        for c in checks:
            if ':' not in c:
                process_range_with_rule(current_part_range, c)
            else:
                param = c[0]
                sign = c[1]
                check_value = int(c[2:].split(':')[0])
                next_rule_name = c.split(':')[1]
                current_range = current_part_range[param]
                if sign == '>':
                    if check_value in current_range:
                        not_matching_range = range(current_range.start, check_value + 1)
                        not_matching_part_range = current_part_range.copy()
                        not_matching_part_range[param] = not_matching_range
                        current_part_range = not_matching_part_range

                        matching_range = range(check_value + 1, current_range.stop)
                        matching_part_range = current_part_range.copy()
                        matching_part_range[param] = matching_range
                        process_range_with_rule(matching_part_range, next_rule_name)
                    elif check_value < current_range.start:
                        process_range_with_rule(current_part_range, next_rule_name)

                else:
                    if check_value in current_range:
                        not_matching_range = range(check_value, current_range.stop)
                        not_matching_part_range = current_part_range.copy()
                        not_matching_part_range[param] = not_matching_range
                        current_part_range = not_matching_part_range

                        matching_range = range(current_range.start, check_value)
                        matching_part_range = current_part_range.copy()
                        matching_part_range[param] = matching_range
                        process_range_with_rule(matching_part_range, next_rule_name)
                    elif check_value > current_range.end:
                        process_range_with_rule(current_part_range, next_rule_name)

    process_range_with_rule(accepted_part_range, 'in')

    def range_combinations(accepted_range):
        result = 1
        for value in accepted_range.values():
            result = result * len(value)
        return result

    return sum(map(range_combinations, accepted_ranges))


sample_data = read_test_input(2023, 19)
data = read_input(2023, 19)

check(part_1(sample_data), 19114)
print(part_1(data))

check(part_2(sample_data), 167409079868000)
print(part_2(data))
