#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

from heap import MaxHeap

m = MaxHeap([95, 3, 21])
m.push(10)
print(m)
print(m.pop())
print(m.peek())
