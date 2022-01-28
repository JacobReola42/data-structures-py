#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

from vertex import Vertex
from graph import Graph

g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']

# Print Header Row
for i in range(ord('A'), ord('K')):
    print(' ', chr(i), end="")
print()

# Print Columns
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

for edge in edges:
    g.add_edge('A', 'B', 2)
    g.add_edge('A', 'E', 3)
    g.add_edge('B', 'F', 4)
    g.add_edge(edge[0], edge[1])

g.print_graph()
