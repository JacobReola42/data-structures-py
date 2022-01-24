#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

# Uses stack data structure
def dfs(data, start, visited):

    if start not in visited:
        print(start, end=" ")

    visited.add(start)  # Add to set

    for i in data[start] - visited:
        dfs(data, i, visited)   # if not visited recursion.
    return

__name__ == '__main__'
visited = set()

# adjacency data in dictionary form
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

dfs(data, 'D', visited)
