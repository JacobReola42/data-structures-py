#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

from singly import LinkedList
from doubly import DoublyLinkedList

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







