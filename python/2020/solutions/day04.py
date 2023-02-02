#!/usr/bin/env python3

from utils.utils import read_input_raw, read_test_input_raw, check


def part_1(data):
    required_fields = ('byr:', 'iyr:', 'eyr:', 'hgt:',
                       'hcl:', 'ecl:', 'pid:')
    passports = data.split('\n\n')

    return sum(all(f in p for f in required_fields) for p in passports)


def part_2(data):
    def check_height(h: str):
        if (h.endswith('cm')):
            return 150 <= int(h[:-2]) <= 193
        elif (h.endswith('in')):
            return 59 <= int(h[:-2]) <= 76
        else:
            return False

    checks = {
        'byr': lambda v: 1920 <= int(v) <= 2002,
        'iyr': lambda v: 2010 <= int(v) <= 2020,
        'eyr': lambda v: 2020 <= int(v) <= 2030,
        'hgt': check_height,
        'hcl': lambda v: len(v) == 7 and v[0] == '#' and all(c.isdigit() or c in 'abcdef' for c in v[1:]),
        'ecl': lambda v: v in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        'pid': lambda v: len(v) == 9 and v.isdigit(),
        'cid': lambda v: True
    }

    def parse(raw): return [field.split(':') for field in raw.split()]
    passports = list(map(parse, data.split('\n\n')))

    valid = 0

    for fields in passports:
        keys = list(map(lambda x: x[0], fields))
        if (all(k in keys for k in list(checks.keys())[:-1])):
            if all(checks[k](v) for k, v in fields):
                valid += 1

    return valid


sample_data = read_test_input_raw(2020, 4)
data = read_input_raw(2020, 4)

check(part_1(sample_data), 2)
print(part_1(data))

check(part_2('''eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007'''), 0)
check(part_2('''pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'''), 4)
print(part_2(data))
