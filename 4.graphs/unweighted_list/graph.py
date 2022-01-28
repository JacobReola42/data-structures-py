#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

from node import Vertex

# Graph is child, inherting Vertex, use with line 12, 13 or without.
class Graph(Vertex):
# class Graph():   # use with line 11 and12

    # Another form of inheritence
    # def __init__(self, nodes, is_directed=False):
    #    Vertex.__init__(self, nodes, is_directed=False)
    #    super().__init__(nodes, is_directed=False)

    def add_edge(self,v,e):
        self.adj_list[v].append(e)
        if not self.is_directed:
            self.adj_list[e].append(v)

    # degree is num of edges incidenting
    def degree_vertex(self,node):   
        degree = len(self.adj_list[node])
        return degree

    def display_adj(self):
        for node in self.nodes:
            print(node,":",self.adj_list[node])
