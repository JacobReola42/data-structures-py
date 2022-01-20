#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

def binarySearch(data, left_Index, right_Index, x):  # Recursive approach

    if right_Index >= left_Index:
        mid_Index = (left_Index + right_Index) // 2
        mid_Num = data[mid_Index]

        # Element is only on the right subarray.
        if mid_Num < x:
            return binarySearch(data, mid_Index + 1, right, x)

        # Element is only on the left subarray.
        elif mid_Num > x:
            return binarySearch(data, left_Index, mid_Index - 1, x)

        #  Element is the middle itself
        else:
            return mid_Index

    return -1

dataList = [11, 12, 33, 66, 77, 83, 95]
xSpot    = 83 
left     = 0
right    = len(dataList) - 1

result  = binarySearch(dataList, left, right, xSpot)

print(f"Number found at index {result}.")
