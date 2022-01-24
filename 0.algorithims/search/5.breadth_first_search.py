#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

# Uses queue data structure
def bfs(data, start, visited=set()):

    queue = [start]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            print(vertex, end=" ")

        visited.add(vertex)

        for i in data[vertex] - visited:
            queue.append(i)
    return


if __name__ == '__main__':

    """
    data = {
        'A': {'B', 'X'},
        'B': {'A', 'C', 'D'},
        'C': {'B', 'E', '4'},
        'D': {'B', 'E', 'F', 'G', 'H', 'I', 'J'},
        'E': {'C', 'D', 'F', '4'},
        'F': {'E', 'J'},
        'G': {'D', 'H'},
        'H': {'D', 'G', 'I'},
        'I': {'D', 'H', 'J'},
        'J': {'D', 'I', 'F'},
        '4': {'F', 'X', 'C'},
        'X': {'4', 'A'}
        }
    """

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
