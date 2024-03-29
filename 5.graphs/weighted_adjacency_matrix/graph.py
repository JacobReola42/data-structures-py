#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

from vertex import Vertex

# Utilizes 2D-Array
class Graph:
    vertices = {}
    edges = []
    edge_indices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            # for loop appends a column of zeros to the edges matrix
            for row in self.edges:
                row.append(0)
            # append a row of zeros to the bottom of the edges matrix
            self.edges.append([0] * (len(self.edges)+1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            return True
        else:
            return False

    def add_edge(self, u, v, weight=1):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]] [self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]] [self.edge_indices[u]] = weight
            return True
        else:
            return False

    def print_graph(self):
        for v, i in sorted(self.edge_indices.items()):
            print(v + ' ', end='')
            for j in range(len(self.edges)):
                print(self.edges[i][j], end='  ')
            print(' ')

