#!/usr/bin/env python3
# Copyright 2022 Jacob Reola, all rights reserved

class TreeNode:

	def __init__(self, val):
		self.value = val
		self.leftChild = None
		self.rightChild = None
		
	def insertNode(self, data):
		if self.value == data:
			return False
			
		elif self.value > data:
			if self.leftChild:
				return self.leftChild.insertNode(data)
			else:
				self.leftChild = TreeNode(data)
				return True

		else:
			if self.rightChild:
				return self.rightChild.insertNode(data)
			else:
				self.rightChild = TreeNode(data)
				return True
				
	def locateNode(self, data):
		if(self.value == data):
			return True
		elif self.value > data:
			if self.leftChild:
				return self.leftChild.locateNode(data)
			else:
				return False
		else:
			if self.rightChild:
				return self.rightChild.locateNode(data)
			else:
				return False
				
	def getSize(self):
		if self.leftChild and self.rightChild:
			return 1 + self.leftChild.getSize() + self.rightChild.getSize()
		elif self.leftChild:
			return 1 + self.leftChild.getSize()
		elif self.rightChild:
			return 1 + self.rightChild.getSize()
		else:
			return 1

	def getHeight(self):
		if self.leftChild and self.rightChild:
			return 1 + max(self.leftChild.getHeight(), self.rightChild.getHeight())
		elif self.leftChild:
			return 1 + self.leftChild.getHeight()
		elif self.rightChild:
			return 1 + self.rightChild.getHeight()
		else:
			return 1

	def preorderNodes(self):
		if self:
			print (str(self.value), end=' ')
			if self.leftChild:
				self.leftChild.preorderNodes()
			if self.rightChild:
				self.rightChild.preorderNodes()

	def inorderNodes(self):
		if self:
			if self.leftChild:
				self.leftChild.inorderNodes()
			print (str(self.value), end=' ')
			if self.rightChild:
				self.rightChild.inorderNodes()

	def postorderNodes(self):
		if self:
			if self.leftChild:
				self.leftChild.postorderNodes()
			if self.rightChild:
				self.rightChild.postorderNodes()
			print (str(self.value), end=' ')
