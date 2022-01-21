#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

from node import TreeNode

class BTree:

	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root:
			return self.root.insertNode(data)
		else:
			self.root = TreeNode(data)
			return True

	def find(self, data):
		if self.root:
			return self.root.locateNode(data)
		else:
			return False
			
	def getHeight(self):
		if self.root:
			return self.root.getHeight()
		else:
			return 0
			
	def getSize(self):
		if self.root:
			return self.root.getSize()
		else:
			return 0
	
	def remove(self, data):
		# empty tree
		if self.root is None:
			return False
			
		# data is in root node	
		elif self.root.value == data:
			if self.root.leftChild is None and self.root.rightChild is None:
				self.root = None
			elif self.root.leftChild and self.root.rightChild is None:
				self.root = self.root.leftChild
			elif self.root.leftChild is None and self.root.rightChild:
				self.root = self.root.rightChild
			elif self.root.leftChild and self.root.rightChild:
				delNodeParent = self.root
				delNode = self.root.rightChild
				while delNode.leftChild:
					delNodeParent = delNode
					delNode = delNode.leftChild
					
				if delNode.rightChild:
					if delNodeParent.value > delNode.value:
						delNodeParent.leftChild = delNode.rightChild
					elif delNodeParent.value < delNode.value:
						delNodeParent.rightChild = delNode.rightChild
				else:
					if delNode.value < delNodeParent.value:
						delNodeParent.leftChild = None
					else:
						delNodeParent.rightChild = None
				self.root.value = delNode.value
						
			return True
		
		parent = None
		node = self.root
		
		# find node to remove
		while node and node.value != data:
			parent = node
			if data < node.value:
				node = node.leftChild
			elif data > node.value:
				node = node.rightChild
		
		# case 1: data not found
		if node is None or node.value != data:
			return False
			
		# case 2: remove-node has no children
		elif node.leftChild is None and node.rightChild is None:
			if data < parent.value:
				parent.leftChild = None
			else:
				parent.rightChild = None
			return True
			
		# case 3: remove-node has left child only
		elif node.leftChild and node.rightChild is None:
			if data < parent.value:
				parent.leftChild = node.leftChild
			else:
				parent.rightChild = node.leftChild
			return True
			
		# case 4: remove-node has right child only
		elif node.leftChild is None and node.rightChild:
			if data < parent.value:
				parent.leftChild = node.rightChild
			else:
				parent.rightChild = node.rightChild
			return True
			
		# case 5: remove-node has left and right children
		else:
			delNodeParent = node
			delNode = node.rightChild
			while delNode.leftChild:
				delNodeParent = delNode
				delNode = delNode.leftChild
				
			node.value = delNode.value
			if delNode.rightChild:
				if delNodeParent.value > delNode.value:
					delNodeParent.leftChild = delNode.rightChild
				elif delNodeParent.value < delNode.value:
					delNodeParent.rightChild = delNode.rightChild
			else:
				if delNode.value < delNodeParent.value:
					delNodeParent.leftChild = None
				else:
					delNodeParent.rightChild = None

	def preorder(self):
		if self.root is not None:
			print("\nPreOrder")
			self.root.preorderNodes()
			
	def inorder(self):
		if self.root is not None:
			print("\nInOrder")
			self.root.inorderNodes()

	def postorder(self):
		if self.root is not None:
			print("\nPostOrder")
			self.root.postorderNodes()
