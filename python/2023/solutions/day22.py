#!/usr/bin/env python3
from utils.utils import read_input, check, read_test_input


def parse_figures(data):
    figures = []
    for line in data:
        raw_start, raw_end = line.split('~')
        x1, y1, z1 = map(int, raw_start.split(','))
        x2, y2, z2 = map(int, raw_end.split(','))
        figure = []
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z in range(z1, z2 + 1):
                    figure.append((x, y, z))
        figures.append(figure)
    return figures


def is_move_possible(figure, settled):
    all_points = set()
    for field_figure in settled:
        for point in field_figure:
            all_points.add(point)
    lowest_z = min(figure, key=lambda f: f[2])[2]
    if lowest_z == 0:
        return False

    new_points = set()
    for x, y, z in figure:
        new_points.add((x, y, z - 1))
    return len(all_points.intersection(new_points)) == 0


def settle(figure, settled):
    while is_move_possible(figure, settled):
        new_figure = []
        for x, y, z in figure:
            new_figure.append((x, y, z - 1))
        figure = new_figure
    return figure


def settle_figures(figures):
    new_figures = []
    for figure in figures:
        new_figures.append(settle(figure, new_figures))
    return new_figures


def build_support_maps(figures):
    points_to_figures = {}
    for i, figure in enumerate(figures):
        for point in figure:
            points_to_figures[point] = i
    figure_to_supports = {}
    figure_to_supported_by = {}
    for i, figure in enumerate(figures):
        for x, y, z in figure:
            supports_point = (x, y, z + 1)
            if supports_point in points_to_figures and points_to_figures[supports_point] != i:
                dependencies_set = figure_to_supports.get(i, set())
                dependencies_set.add(points_to_figures[supports_point])
                figure_to_supports[i] = dependencies_set
            support_point = (x, y, z - 1)
            if support_point in points_to_figures and points_to_figures[support_point] != i:
                dependencies_set = figure_to_supported_by.get(i, set())
                dependencies_set.add(points_to_figures[support_point])
                figure_to_supported_by[i] = dependencies_set
    return figure_to_supported_by, figure_to_supports


def part_1(data):
    figures = parse_figures(data)

    figures.sort(key=lambda figure: min(map(lambda point: point[2], figure)))

    figures = settle_figures(figures)

    figure_to_supported_by, figure_to_supports = build_support_maps(figures)

    result = 0

    for i in range(len(figures)):
        supported = figure_to_supports.get(i, [])
        everything_is_double_supported = all(len(figure_to_supported_by.get(figure, [])) > 1 for figure in supported)
        if everything_is_double_supported:
            result = result + 1

    return result


def part_2(data):
    figures = parse_figures(data)

    figures.sort(key=lambda figure: min(map(lambda point: point[2], figure)))

    figures = settle_figures(figures)

    figure_to_supported_by, figure_to_supports = build_support_maps(figures)

    def find_supported(index):
        to_check = {index}
        dropped = set()
        while to_check:
            current = to_check.pop()
            immediately_supported = figure_to_supports.get(current, set())
            for supported in immediately_supported:
                if len(figure_to_supported_by.get(supported, []) - dropped - {index}) == 0:
                    to_check.add(supported)
                    dropped.add(supported)

        return dropped

    each_figure_supports = list(map(find_supported, range(len(figures))))
    return sum(map(len, each_figure_supports))


sample_data = read_test_input(2023, 22)
data = read_input(2023, 22)

check(part_1(sample_data), 5)
print(part_1(data))

check(part_2(sample_data), 7)
print(part_2(data))
