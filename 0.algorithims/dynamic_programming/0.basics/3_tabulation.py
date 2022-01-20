#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

# Opposite of memoization i.e. this is botom-up.

def fibonacci(num):
    dynamicProgram = [0, 1]
    for i in range (2, num + 1):
        dynamicProgram.append(dynamicProgram[i-1] + dynamicProgram[i-2])

    return dynamicProgram[num]

__name__ == '__main__'

for i in range(4, 10):
    print(f"{i}th Fibonacci is ---> " + str(fibonacci(i)))
