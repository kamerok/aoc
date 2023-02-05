#!/usr/bin/env python3

from utils.utils import check, read_test_input, read_input

SHINY_GOLD = 'shiny gold'


def main():
    sample_data = read_test_input(2020, 7)
    sample_data2 = read_input(2020, 7, '_test2')
    data = read_input(2020, 7)

    check(part_1(sample_data), 4)
    print(part_1(data))

    check(part_2(sample_data), 32)
    check(part_2(sample_data2), 126)
    print(part_2(data))


def part_1(data):
    rules = parse_input(data)
    other_bags = list(rules.keys())
    other_bags.remove(SHINY_GOLD)

    def bag_contains_shiny(bag):
        return contains_shiny(bag, rules)

    return sum(map(bag_contains_shiny, other_bags))


def part_2(data):
    rules = parse_input(data)
    return count_bags(SHINY_GOLD, rules) - 1


def parse_input(data):
    def parse_entry(entry):
        bag, content_raw = entry.split(' bags contain ')
        bag_contents_raw = content_raw.split(', ')

        def map_content_entry(content_entry_raw):
            words = content_entry_raw.split()
            if words[0] == 'no':
                return None
            else:
                return ' '.join(words[1:3]), int(words[0])

        content = dict(filter(
            lambda c: c is not None,
            map(map_content_entry, bag_contents_raw)
        ))
        return bag, content

    return dict(map(parse_entry, data))


def contains_shiny(bag, rules):
    bags_inside = rules[bag]

    if SHINY_GOLD in bags_inside:
        return True

    return any(contains_shiny(bag, rules) for bag in bags_inside.keys())


def count_bags(bag, rules):
    bags_inside = rules[bag]

    result = 1

    for bag, count in bags_inside.items():
        result += count_bags(bag, rules) * count

    return result


if __name__ == '__main__':
    main()
