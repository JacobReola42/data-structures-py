#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

# Parent
class Vertex:
    def __init__(self, Nodes, is_directed=False):
        self.nodes = Nodes
        self.adj_list = dict()  #{}
        self.is_directed = is_directed

       # for node in self.nodes:
       #     self.adj_list[node] = list()
