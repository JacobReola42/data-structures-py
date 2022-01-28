#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

# Uses queue data structure

import collections

def bfs(data, start):

    visited, queue = set(), collections.deque([start])
    visited.add(start)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in data[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

__name__ == '__main__'

data = {
    'A': {'B'},
    'B': {'A', 'C', 'D'},
    'C': {'B', 'E'},
    'D': {'B', 'E'},
    'E': {'C', 'D', 'F', '4'},
    'F': {'E'},
    '4': {'F', 'X'},
    'X': {'4'}
    }

bfs(data, 'C')
