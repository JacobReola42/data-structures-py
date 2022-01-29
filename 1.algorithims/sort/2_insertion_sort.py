#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

def insertionSort(data):
    arrayLength = len(data)

    for i in range(1, arrayLength):
        anchorKey = data[i]     # Key to be inserted.
        element = i-1           # If element is greater than achhor key, move one position ahead of current.

        while element >= 0 and anchorKey < data[element]:
            data[element + 1] = data[element]
            element -= 1
        data[element + 1] = anchorKey

__name__ == "__main__"

data = [191991, 34, 11, 23, 99, 2000, 999999999, 1,2,3334,5, 99, 1080, 888]

print('\nCurrent array is:', data,'\n')

insertionSort(data)
print('Sorted array is:', data, '\n')

dataLength = len(data)
for i in range(dataLength):
    print("%d" %data[i],)

print()

"""
To sort an array of size n in ascending order:
1: Iterate from arr[1] to arr[n] over the array.
2: Compare the current element (key) to its predecessor.
3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.
Example:
"""
