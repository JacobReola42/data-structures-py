#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

from graph import Graph
from node import Vertex

edges = [ ("A","B"),
          ("A","C"),
          ("B","C"),
          ("B","D"),
          ("B","E"),
          ("C","D"),
          ("D","E")
        ]

nodes=["A","B","C","D","E"]

# Change to true for unique values
graph = Graph(nodes, is_directed=False)

for node in graph.nodes:
    graph.adj_list[node] = list()

for v,e in edges:
    graph.add_edge(v,e)

graph.display_adj()

print(graph.degree_vertex("C"))
