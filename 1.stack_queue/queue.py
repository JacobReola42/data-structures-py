#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

from collections import deque

class Queue:
    
    def __init__(self):
       self.queue = deque()
       self.size = 0
       self.front = 0

    def __len__(self):
        return self.size 

    def isEmpty(self):
        return self.size == 0
            
    # append right
    def enqueue(self, element):
        self.queue.append(element)
        self.size += 1

    def peek(self):
        if self.isEmpty():
            return("CAN'T PEEK, EMPTY!")
        return self.queue[self.front]

    # pop left
    def dequeue(self):
        if self.isEmpty():
            return ("CAN'T DEQUEUE, EMPTY!")
        
        answer = self.queue[self.front]
        self.queue[self.front] = None   # helps with garbage collection
        self.front = (self.front + 1) % len(self.queue)
        self.size -= 1
        return answer

    def getSize(self):
        return self.size
            



