#!/usr/bin/env python3
from collections import deque

from utils.utils import check


def main():
    data = (1, 12, 0, 20, 8, 16)

    check(solve((0, 3, 6)), 436)
    check(solve((1, 3, 2)), 1)
    check(solve((2, 1, 3)), 10)
    check(solve((1, 2, 3)), 27)
    check(solve((2, 3, 1)), 78)
    check(solve((3, 2, 1)), 438)
    check(solve((3, 1, 2)), 1836)
    print(solve(data))

    check(solve((0, 3, 6), 30000000), 175594)
    check(solve((1, 3, 2), 30000000), 2578)
    check(solve((2, 1, 3), 30000000), 3544142)
    check(solve((1, 2, 3), 30000000), 261214)
    check(solve((2, 3, 1), 30000000), 6895259)
    check(solve((3, 2, 1), 30000000), 18)
    check(solve((3, 1, 2), 30000000), 362)
    print(solve(data, 30000000))


def solve(data, stop=2020):
    cache = {}
    for i, n in enumerate(data):
        cache[n] = deque([i])

    last_number = data[-1]

    for i in range(i + 1, stop):
        if last_number in cache:
            indexes = cache[last_number]
            last_number = i - 1 - indexes[-1]
            indexes.append(i - 1)
            if len(indexes) > 2:
                indexes.popleft()
        else:
            cache[last_number] = deque([i - 1])
            last_number = 0

    return last_number


if __name__ == '__main__':
    main()
