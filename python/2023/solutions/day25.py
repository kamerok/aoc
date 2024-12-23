#!/usr/bin/env python3
import gravis as gv
import networkx as nx

from utils.utils import read_input, check, read_test_input


def generate_graph(data):
    edges = []
    for line in data:
        node, raw_linked = line.split(': ')
        linked = set(raw_linked.split())
        for l in linked:
            edges.append((node, l))
    g = nx.DiGraph()
    g.add_edges_from(edges)
    fig = gv.d3(g)
    fig.export_html('graph.html')


def part_1(data):
    # received from generated force directed graphs
    nodes_to_remove = (('nvd', 'jqt'), ('cmg', 'bvb'), ('pzl', 'hfx'),
                       ('vmq', 'cbl'), ('nvf', 'bvz'), ('xgz', 'klk'))

    connections = {}
    for line in data:
        node, raw_linked = line.split(': ')
        linked = set(raw_linked.split())
        connections[node] = {*connections.get(node, set()), *linked}
        for linked_node in linked:
            connections[linked_node] = {*connections.get(linked_node, set()), node}

    for n1, n2 in nodes_to_remove:
        if n1 in connections and n2 in connections:
            connections[n1].remove(n2)
            connections[n2].remove(n1)

    nodes = set(connections.keys())
    group_1 = set()
    to_visit = [nodes.pop()]
    while to_visit:
        node = to_visit.pop()
        group_1.add(node)
        next_nodes = connections[node]
        for next_node in next_nodes:
            if next_node in nodes:
                nodes.remove(next_node)
                to_visit.append(next_node)

    group_2 = set()
    to_visit = [nodes.pop()]
    while to_visit:
        node = to_visit.pop()
        group_2.add(node)
        next_nodes = connections[node]
        for next_node in next_nodes:
            if next_node in nodes:
                nodes.remove(next_node)
                to_visit.append(next_node)

    return len(group_1) * len(group_2)


sample_data = read_test_input(2023, 25)
input_data = read_input(2023, 25)

check(part_1(sample_data), 54)
print(part_1(input_data))
