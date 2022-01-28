#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

class Graph:
    def __init__(self,Nodes,is_directed=False):
        self.nodes = Nodes
        self.adj_list = dict()
        self.is_directed = is_directed

       # for node in self.nodes:
       #     self.adj_list[node] = list()

    # v=vertex, e=edge
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
