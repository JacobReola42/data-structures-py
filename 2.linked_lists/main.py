#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

from singly import LinkedList
from doubly import DoublyLinkedList
from circularly import CircularLinkedList

# SINGLY
print('\nTESTING SINGLY LINKED LIST')
myList = LinkedList()

print('\nCreating a singly link list.' )
print('Top of the link list is:', myList.top())
print('The list is empty:', myList.isEmpty())
print('Inputting values into link list . . .\n' )
myList.add(55)
myList.add(8)
myList.add(12)
myList.add(22)
myList.displayList()
print('The list is empty:', myList.isEmpty())
print('Top of the link list is:', myList.top())
print('Checking for number 12 in list.', myList.locate(12), 'is found.')
print("Current size of list is","size="+str(myList.size))
print()

print('Removing number 8')
myList.remove(8)
myList.displayList()
print("Current size of list is","size="+str(myList.size))
print()

print('Removing number 22')
myList.remove(22)
myList.displayList()
print('Top of the link list is:', myList.top())
print("Current size of list is","size="+str(myList.size))
print('Checking for number 5 in list:', myList.locate(5))
print('The head of the list is now:', myList.head)
print()

# DOUBLY
print('TESTING DOUBLY LINKED LIST\n')
dll = DoublyLinkedList()

print('Creating doubly linked list . . . ')
print('The list is empty:', dll.isEmpty())
print('Inputting Values')

for i in [22,33,44,55,66,77]:
    dll.add(i)

dll.print_list()
print('The list is empty:', dll.isEmpty())
print('Deleting 44:', dll.remove(44))

dll.print_list()
print("size="+str(dll.size))
print()

# CIRCULARLY
print('TESTING CIRCULARLY LINKED LIST\n')
cll = CircularLinkedList()

for i in [5, 7, 3, 8, 9]:
    cll.add(i)

print('Test 1.')
print("size="+str(cll.size))
print(cll.find(8))
print(cll.find(12))

my_node = cll.root
print (my_node, end='->')

for i in range(8):
    my_node = my_node.nxt_node
    print (my_node, end='->')

print('\n\nTest 2.')
cll.print_list()
cll.remove(8)
print(cll.remove(15))
print("size="+str(cll.size))
cll.remove(5)    # delete root node
cll.print_list()
