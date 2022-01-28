#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

from node import Vertex

# inheriting 
class Graph(Vertex):

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
