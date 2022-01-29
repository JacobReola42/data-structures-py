#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

from binary import BTree

bst = BTree()

print('\nInputting values to tree.')

for i in [15, 10, 2, 12, 3, 1, 13, 6, 11, 4, 14, 9]:
    bst.insert(i)

print('Size = ', bst.getSize())
print('Height is:', bst.getHeight())
print('locating 13:', bst.find(13))
bst.preorder()
bst.inorder()
bst.postorder()
print('\n\nLocating 14:', bst.find(14))
print('Removing 10. Is it in the list?', bst.remove(10))
bst.inorder()
