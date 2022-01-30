#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

# Fibonacci numbers are a series of numbers in which each number is the sum of the two preceding numbers. 


def fibonacci(num):     # Non-dynamic recursive method
    if num < 2:         # Base condition to 1
        return num

    return fibonacci(num-1) + fibonacci(num-2)

__name__ == '__main__'

for i in range(4, 10):
    print(f"{i}th Fibonacci is ---> " + str(fibonacci(i)))

## This method contains overlapping subproblem patterns. 
## See memoization.py

"""
Source: Grokking
"""
