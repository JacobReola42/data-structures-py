#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

from vertex import Vertex

class Graph:
	vertices = {}
	
	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False
	
	def add_edge(self, u, v, weight=0):
		if u in self.vertices and v in self.vertices:
			# can use a loop, but this is a much faster way to do it
			self.vertices[u].add_neighbor(v, weight)
			self.vertices[v].add_neighbor(u, weight)
			return True
		else:
			return False
			
	def print_graph(self):
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].neighbors))
