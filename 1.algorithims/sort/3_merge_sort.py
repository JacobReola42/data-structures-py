#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

def mergeSort(data):
    
    if len(data) > 1:   # Base case
        middle_index = len(data) // 2

        # Divide array data left and right
        left_array  = data[:middle_index]
        right_array = data[middle_index:]

        # Sort the left half then other.
        mergeSort(left_array)
        mergeSort(right_array)

        i = j = k = 0

        # Copy data to left and right temp arrays
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                data[k] = left_array[i]
                i += 1
            else:
                data[k] = right_array[j]
                j += 1
            k += 1

        # Check if any element is left
        while i < len(left_array):
            data[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            data[k] = right_array[j]
            j += 1
            k += 1

def displayList(data):
    arrayLength = len(data)

    for i in range(arrayLength):
        print(data[i], end=" ")
    print()


__name__ == "__main__"

data = [19, 34, 11, 23, 99, 10, 1111, 8888, 9999, 123214, 99, 2]

displayList(data)
mergeSort(data)
displayList(data)

