#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

from node import Node

class LinkedList:
    
    def __init__(self, head = None):
        self.head = head
        self.size = 0

    def add(self, element):
        newNode= Node(element, self.head)
        self.head = newNode
        self.size += 1

    def isEmpty(self):
        return self.size == 0 

    def top(self):
        if self.isEmpty():
            return ('None')
        else:
            return self.head.data

    def locate(self, element):
        this_node = self.head
        while this_node is not None:
            if this_node.data == element:
                return element 
            else:
                this_node = this_node.nxt_node

    def remove(self, element):
        this_node = self.head
        prev_node = None

        while this_node is not None:
            if this_node.data == element:
                if prev_node is not None:
                    prev_node.nxt_node = this_node.nxt_node
                else:
                    self.head = this_node.nxt_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.nxt_node
        return False

    def displayList(self):
        this_node = self.head
        while this_node is not None:
            print(this_node, end='->')
            this_node = this_node.nxt_node
        print('None')
