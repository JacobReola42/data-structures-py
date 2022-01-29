#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

# memoization is top down dynamic programming i.e. dp[n]


def fibonacci(num):
    memoize = [-1 for x in range(num + 1)]
    return fibonacciRecursively(memoize, num)

def fibonacciRecursively(memoize, num):
    if num < 2:         # Base condition to 1
        return num

    # If subproblem is solved, return result from the cache
    if memoize[num] >= 0:
        return memoize[num]

    memoize[num] = fibonacciRecursively(memoize, num - 1) + fibonacciRecursively(memoize, num - 2)  

    return memoize[num]


__name__ == '__main__'

for i in range(4, 10):
    print(f"{i}th Fibonacci is ---> " + str(fibonacci(i)))
