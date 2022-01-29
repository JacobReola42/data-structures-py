#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

class Node:
    def __init__(self, element, nxt = None, prev = None):
        self.data = element 
        self.nxt_node = nxt
        self.prev_node = prev

    def __str__(self):
        return ( '('+ str(self.data) +')' )
