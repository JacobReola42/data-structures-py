#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

from stack import ArrayStack
from queue import Queue

print('TESTING STACK')

myStack = ArrayStack()

print('Is the stack empty?', myStack.isEmpty())
print('There are', len(myStack), 'elements in the stack.\n')

print('Pushing elements into stack . . . ', '\n' )

myStack.push(11)
myStack.push(22)
myStack.push(33)

print('Is the stack empty?', myStack.isEmpty())
print('There are', len(myStack), 'elements in the stack.\n')

print('Top of the Stack contains the element:', myStack.peek())
print('Popping from the stack:', myStack.pop(), '\n')

print('Top of the Stack contains the element:', myStack.peek())
print('Popping from the stack:', myStack.pop())

print('There are', len(myStack), 'elements in the stack.\n')

print('Top of the Stack contains the element:', myStack.peek())
print('Popping from the stack:', myStack.pop(), '\n')

print('Popping from the stack:', myStack.pop())


print('Is the stack empty?', myStack.isEmpty())
print('There are', len(myStack), 'elements in the stack.')


print('\nTESTING QUEUE\n')

myQueue = Queue()

print('Creating empty stack:', myQueue.isEmpty())
print('Getting size of stack using len():', len(myQueue))
print('Getting size of stack using getSize():', myQueue.getSize())
print()

print('Displaying current queue:', list(myQueue.queue))
print(myQueue.dequeue())
print(myQueue.peek())

print('\nInputting elements in queue')
myQueue.enqueue(99)
myQueue.enqueue(88)
myQueue.enqueue(77)
myQueue.enqueue(66)
myQueue.enqueue(55)
print('Queue contains:', list(myQueue.queue), '\n')

print('Deque queue:', myQueue.dequeue())
print('Displaying current queue:',list(myQueue.queue))
print('Displaying first in queue:', myQueue.peek())
print('Getting size of stack using len():', len(myQueue))
print('Getting size of stack using getSize():', myQueue.getSize(), '\n')

print('Emptying Queue . . .')
myQueue.dequeue()
myQueue.dequeue()
print('Is queue empty:', myQueue.isEmpty())
print('First in queue is:', myQueue.peek())
print('Displaying current queue:',list(myQueue.queue))
print('Getting size of stack using len():', len(myQueue))
print('Getting size of stack using getSize():', myQueue.getSize(), '\n')

print('Emptying Queue . . .')
myQueue.dequeue()
myQueue.dequeue()

print('Queue contains:', list(myQueue.queue))
print('Is queue empty:', myQueue.isEmpty())
print('First in queue is:', myQueue.peek())
print('Current size of queue:', myQueue.getSize(), '\n')
