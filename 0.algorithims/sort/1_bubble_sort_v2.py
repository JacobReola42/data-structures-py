#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

# OPTIMIZED VERSION by stopping the algo if the inner loop didn't swap.
# Previous version ran on O(n*n).

def bubbleSort(data):
    num = len(data)

    for i in range(num):
        swapped = False
        for j in range(0, num-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True

        # If no two elements were swapped then break.
        if swapped == False:
            break

__name__ == "__main__"

data = [111, 888, 22, 899, 1, 15, 10009, 1080, 7]
print('\nCurrent array:', data,'\n')

bubbleSort(data)
dataLength = len(data)

print("Sorted array")
for i in range(dataLength):
    print("%d" %data[i])
print()
