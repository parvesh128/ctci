#!/bin/python

import sys


class Heap:

	def __init__(self):

		self.val = []
		self.size = 0

	def heapifyUp(self):
		raise NotImplementedError("Subclass must implement abstract method")

	def heapifyDown(self):
		raise NotImplementedError("Subclass must implement abstract method")

	def push(self, elem):
		self.val.append(elem)
		self.size += 1
		self.heapifyUp()

	def top(self):
		if self.size == 0:
			return None
		return float(self.val[0])

	def pop(self):
		if self.size == 0:
			return None
		ret = self.val[0]
		self.size -= 1

		if self.size > 0:
			self.val[0] = self.val.pop()
			self.heapifyDown()
		else:
			self.val.pop()
		return ret

	def hasParent(self, index):
		if (index - 1) / 2 >= 0:
			return True
		return False

	def getParentIndex(self, index):
		return (index - 1) / 2

	def hasLeftChild(self, index):
		if (2 * index + 1) < self.size:
			return True
		return False

	def hasRightChild(self, index):
		if (2 * index + 2) < self.size:
			return True
		return False

	def getLeftChildIndex(self, index):
		return 2 * index + 1

	def getRightChildIndex(self, index):
		return 2 * index + 2

	def swap(self, index1, index2):
		if index1 < 0 or index1 >= self.size\
			or index2 < 0 or index2 >= self.size:
			raise Exception('Invalid arguments to swap')

		temp = self.val[index1]
		self.val[index1] = self.val[index2]
		self.val[index2] = temp

	def __repr__(self):
		return str(self.val)

	__str__ = __repr__



class MinHeap(Heap):

	def heapifyUp(self):
		index = self.size - 1

		while self.hasParent(index):
			parentIndex = self.getParentIndex(index)
			
			if self.val[parentIndex] <= self.val[index]:
				break

			self.swap(index, parentIndex)
			index = parentIndex

	def heapifyDown(self):
		index = 0

		while self.hasLeftChild(index):
			smallestIndex = index

			leftChildIndex = self.getLeftChildIndex(index)

			if self.val[leftChildIndex] < self.val[smallestIndex]:
				smallestIndex = leftChildIndex

			if self.hasRightChild(index):
				rightChildIndex = self.getRightChildIndex(index)

				if self.val[rightChildIndex] < self.val[smallestIndex]:
					smallestIndex = rightChildIndex

			if index == smallestIndex:
				break

			self.swap(index, smallestIndex)
			index = smallestIndex

class MaxHeap(Heap):

	def heapifyUp(self):
		index = self.size - 1

		while self.hasParent(index):
			parentIndex = self.getParentIndex(index)
			
			if self.val[parentIndex] >= self.val[index]:
				break

			self.swap(index, parentIndex)
			index = parentIndex

	def heapifyDown(self):
		index = 0

		while self.hasLeftChild(index):
			largestIndex = index

			leftChildIndex = self.getLeftChildIndex(index)

			if self.val[leftChildIndex] > self.val[largestIndex]:
				largestIndex = leftChildIndex

			if self.hasRightChild(index):
				rightChildIndex = self.getRightChildIndex(index)

				if self.val[rightChildIndex] > self.val[largestIndex]:
					largestIndex = rightChildIndex

			if index == largestIndex:
				break

			self.swap(index, largestIndex)
			index = largestIndex


def signum(l_size, r_size):
	if l_size == r_size:
		return 0

	return 1 if l_size > r_size else -1


def getMedian(val, prevMedian, left, right):

	sig = signum(left.size, right.size)

	if sig == 0:
		# Both the heaps are equal
		if val < prevMedian:
			# Add to left
			left.push(val)
			return left.top()
		right.push(val)
		return right.top()
	elif sig == 1:
		if val > prevMedian:
			right.push(val)
		else:
			right.push(left.pop())
			left.push(val)
		return (left.top() + right.top()) / 2
	else:
		if val < prevMedian:
			left.push(val)
		else:
			left.push(right.pop())
			right.push(val)
		return (left.top() + right.top()) / 2



n = int(raw_input().strip())
a = []
a_i = 0
median = 0
left = MaxHeap()
right = MinHeap()
for a_i in xrange(n):
    a_t = int(raw_input().strip())
    a.append(a_t)
    
    median = getMedian(a_t, median, left, right)
    print ("%.1f"%(median))
