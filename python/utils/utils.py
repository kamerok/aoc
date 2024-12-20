#!/usr/bin/env python3
import heapq
import os
import sys


def check(value, expected):
    assert value == expected, f'Expected {expected} but was {value}'


def read_input(year, day, suffix=''):
    return read_file_lines(get_file_path(year, day, suffix))


def read_input_raw(year, day, suffix=''):
    with open(get_file_path(year, day, suffix)) as file:
        return file.read()


def read_test_input(year, day):
    return read_input(year, day, '_test')


def read_test_input_raw(year, day):
    return read_input_raw(year, day, '_test')


def get_file_path(year, day, suffix=''):
    file_name = f'day{day:02d}{suffix}.txt'
    # notebook working directory support
    if os.getcwd().endswith('solutions'):
        return f'../inputs/{file_name}'
    else:
        return f'./python/{year}/inputs/{file_name}'


def read_file_lines(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines


def restore_path(point, previous_node):
    path = []
    current_node = point
    while current_node in previous_node:
        path.insert(0, current_node)
        current_node = previous_node[current_node]
    return path


def dijkstra(start, check_end, distance, find_neighbours):
    queue = [(0, start)]
    visited = set()
    previous_node = {}

    min_distance = sys.maxsize

    while len(queue) > 0:
        current_distance, current_node = heapq.heappop(queue)

        neighbours = find_neighbours(current_node)

        for neighbour in neighbours:
            if neighbour not in visited:
                previous_node[neighbour] = current_node
                visited.add(neighbour)

                new_distance = current_distance + distance(neighbour)

                if check_end(neighbour):
                    min_distance = min(min_distance, new_distance)

                heapq.heappush(queue, (new_distance, neighbour))

    return min_distance


def a_star(start, check_end, distance, find_neighbours, heuristic):
    """

    :param start:
    :param check_end:
    :param distance:
    :param find_neighbours:
    :param heuristic: estimation of the cost to reach the end
    :return:
    """
    path = a_star_path(start, check_end, distance, find_neighbours, heuristic)
    if path is None:
        return None

    length = distance(start, path[0])
    for i in range(len(path) - 1):
        length = length + distance(path[i], path[i + 1])
    return length


def a_star_path(start, check_end, distance, find_neighbours, heuristic):
    """

    :param start:
    :param check_end:
    :param distance:
    :param find_neighbours:
    :param heuristic: estimation of the cost to reach the end
    :return:
    """
    queue = [(0, start)]
    previous_node = {}

    g_score = {start: 0}
    f_score = {start: heuristic(start)}

    while len(queue) > 0:
        current_f_score, current = heapq.heappop(queue)

        if check_end(current):
            path = restore_path(current, previous_node)
            return path

        neighbours = find_neighbours(current)

        for neighbour in neighbours:
            tentative_g_score = g_score[current] + distance(current, neighbour)

            if tentative_g_score < g_score.get(neighbour, sys.maxsize):
                previous_node[neighbour] = current
                g_score[neighbour] = tentative_g_score
                neighbour_f_score = tentative_g_score + heuristic(neighbour)
                f_score[neighbour] = neighbour_f_score
                heapq.heappush(queue, (neighbour_f_score, neighbour))

    return None
