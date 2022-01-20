#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

def linearSearch(data, num, x):

    lenData = len(num)

    for i in range(0, lenData):
        if data[i] == x:
            return i
    return -1

__name__ == "__main__"

someData = [1, 22, 33, 44, 55, 77, 88, 99]
find = 99 
x = linearSearch(someData, someData ,find)

print(f"Number found at index {x}.")
