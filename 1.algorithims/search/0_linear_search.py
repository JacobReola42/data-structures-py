#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

def linearSearch(data, num):
    for i, element in enumerate(data):
        if element == num:
            return i
    return -1

__name__ == "__main__"

someData = [1, 22, 33, 44, 55]
find = 33 
x = linearSearch(someData, 33)

print(f"Number found at index {x}.")
