#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

def binarySearch(data, x):  # Iterative approach
    left_Index   = 0
    middle_Index = 0
    right_Index  = len(data) - 1

    while left_Index <= right_Index:
        mid_Index = (left_Index + right_Index) // 2
        mid_Num = data[mid_Index]

        # If x greater, ignore left half 
        if mid_Num < x:
            left_Index = mid_Index + 1

        # If x is less, ignore right half 
        elif mid_Num > x:
            right_Index = mid_Index - 1

        # x marks the spot, middle
        else:
            return mid_Index

    return -1


__name__ == "__main__"

dataList = [11, 12, 33, 66, 77, 83, 95]
xSpot    = 83 

result  = binarySearch(dataList, xSpot)

print(f"Number found at index {result}.")

"""
*This search algorithm takes advantage of a collection of elements that is already sorted by ignoring half of the elements after just one comparison.*
*i.e. If this list of numbers were randomized, you would need to sort it in order.*

Compare x with the middle element.
If x matches with the middle element, we return the mid index.
Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.
Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.

"""
