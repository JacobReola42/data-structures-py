#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

def bubbleSort(data):
    num = len(data)

    for i in range(num):
        for j in range(0, num-i-1):     # Last i elements are in place.
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

__name__ == "__main__"

data = [111, 888, 22, 899, 1, 15, 10009, 1080, 7]
print('\nCurrent array:', data,'\n')

bubbleSort(data)
dataLength = len(data)

print("Sorted array")
for i in range(dataLength):
    print("%d" %data[i])
print()



"""

Works by repeatedly swapping the adjacent elements if they are in wrong order.

First Pass:
( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1. 
( 1 5 4 2 8 ) –> ( 1 4 5 2 8 ), Swap since 5 > 4 
( 1 4 5 2 8 ) –> ( 1 4 2 5 8 ), Swap since 5 > 2 
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.
Second Pass: 
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ) 
( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2 
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) 
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) 
The array is already sorted, However the  algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.
Third Pass: 
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) 
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) 
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) 
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) 

"""
