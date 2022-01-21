#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

# handles sorting of quick sort.
def partition(start_index, end_index, data):
    
    pivot_index = start_index
    pivot = data[pivot_index]

    # When the pointer crosses end pointer,
    # swap pivot with element on end pointer
    while start_index < end_index:
        start_index += 1

        # Increment the start pointer, until it finds the element greater than pivot.
        while start_index < len(data) and data[start_index] <= pivot:
            start_index += 1

        # Decrement end pointer until it finds the element less than pivot.
        while data[end_index] > pivot:
            end_index -= 1

        # If pointers cross, swap the start and end numbers
        if start_index < end_index:
            data[start_index], data[end_index] = data[end_index], data[start_index]

    # Swap pivot element with element on end pointer which puts pivot on correct sorted position
    data[end_index], data[pivot_index] = data[pivot_index], data[end_index]

    # return end pointer // array into 2
    return end_index

def quickSort(start_index, end_index, data):

    if start_index < end_index:
        # partitioning index is at correct position.

        partitioning_index = partition(start_index, end_index, data)

        # Sort elements before and after parition 
        quickSort(start_index, partitioning_index - 1, data)
        quickSort(partitioning_index + 1, end_index, data)


__name__ == "__main__"

data = [77, 23, 44, 9100000, 1, 7, 8, 91212, 128, 2]
dataLength = len(data)

quickSort(0, dataLength - 1, data)
print(f'Sorted array: {data}')
