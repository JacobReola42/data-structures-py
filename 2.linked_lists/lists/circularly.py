#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

from node import Node

class CircularLinkedList:

    def __init__ (self, root = None):
        self.root = root
        self.size = 0

    def add (self, data):
        if self.size == 0:
            self.root = Node(data)
            self.root.nxt_node = self.root
        else:
            new_node = Node (data, self.root.nxt_node)
            self.root.nxt_node = new_node
        self.size += 1

    def find (self, data):
        this_node = self.root
        while True:
            if this_node.data == data:
                return data
            elif this_node.nxt_node == self.root:
                return False
            this_node = this_node.nxt_node

    def remove (self, data):
        this_node = self.root
        prev_node = None

        while True:
            if this_node.data == data:   # found
                if prev_node is not None:
                    prev_node.nxt_node = this_node.nxt_node
                else:
                    while this_node.nxt_node != self.root:
                        this_node = this_node.nxt_node
                    this_node.nxt_node = self.root.nxt_node
                    self.root = self.root.nxt_node
                self.size -= 1
                return True     # data removed
            elif this_node.nxt_node == self.root:
                return False    # data not found
            prev_node = this_node
            this_node = this_node.nxt_node
        
    def print_list (self):
        if self.root is None:
            return
        this_node = self.root
        print (this_node, end='->')
        while this_node.nxt_node != self.root:
            this_node = this_node.nxt_node
            print (this_node, end='->')
        print()
