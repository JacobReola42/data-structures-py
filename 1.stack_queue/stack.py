#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

class ArrayStack:

    def __init__(self):
        self.stack = list()

    def __len__(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, element):
        self.stack.append(element)

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.stack[len(self.stack) -1]

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()

