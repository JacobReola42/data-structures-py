#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

from node import Node

class DoublyLinkedList:

    def __init__(self, root = None):
        self.head = root 
        self.tail = root
        self.size = 0
        
    def add (self, element):
        if self.size == 0:
            self.head = Node(element)
            self.tail = self.head
        else:
            new_node = Node(element, self.head)
            self.head.prev_node = new_node
            self.head = new_node
        self.size += 1

    def isEmpty(self):
        return self.size == 0

    def locate(self, element):
        this_node = self.head
        while this_node is not None:
            if this_node.data == element:
                return element
            elif this_node.nxt_node == None:
                    return False
            else:
                this_node = this_node.nxt_node

    def remove(self, element):
        this_node = self.head
        while this_node is not None:
            if this_node.data == element:
                if this_node.prev_node is not None:
                    if this_node.nxt_node is not None:  # Middle Node
                        this_node.prev_node.nxt_node = this_node.nxt_node
                        this_node.nxt_node.prev_node = this_node.prev_node
                    else: # Delete Tail
                        this_node.prev_node.nxt_node = None
                        self.tail = this_node.prev_node
                else: # Delete head
                    self.head = this_node.nxt_node
                    this_node.nxt_node.prev_node = self.head
                self.size -= 1
                return True # element removed
            else:
                this_node = this_node.nxt_node
        return False    # not found


    def print_list (self):
        if self.head is None:
            return
        this_node = self.head
        print (this_node, end='->')
        while this_node.nxt_node is not None:
            this_node = this_node.nxt_node
            print (this_node, end='->')
        print()

