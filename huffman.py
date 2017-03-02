#!/usr/bin/env python3
import collections



def string2freq(x):
	f = []
	test = collections.Counter(x)
	S = sorted(test.keys())
	#S = sorted(S)

	for n in S:
		f.append(test.get(n))

	#print(S)
	#print(f)
	return S,f

class huffmanEncode:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0


	def percUp(self,i):
		while i // 2 > 0:
			if self.heapList[i] < self.heapList[i // 2]:
				tmp = self.heapList[i // 2]
				self.heapList[i // 2] = self.heapList[i]
				self.heapList[i] = tmp
			i = i // 2

	def insert(self,k):
		self.heapList.append(k)
		self.currentSize = self.currentSize + 1
		self.percUp(self.currentSize)
		print(self.heapList)

	def percDown(self,i):
		while (i * 2) <= self.currentSize:
			mc = self.minChild(i)
			if self.heapList[i] > self.heapList[mc]:
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[mc]
				self.heapList[mc] = tmp
			i = mc

	def minChild(self,i):
		if i * 2 + 1 > self.currentSize:
			return i * 2
		else:
			if self.heapList[i*2] < self.heapList[i*2+1]:
				return i * 2
			else:
				return i * 2 + 1

	def delMin(self):
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize = self.currentSize - 1
		self.heapList.pop()
		self.percDown(1)
		return retval

	def buildHeap(self,alist):
		i = len(alist) // 2
		self.currentSize = len(alist)
		self.heapList = [0] + alist[:]
		while (i > 0):
			self.percDown(i)
			i = i - 1

	#T = {}
	#return T



def encodeString(x,T):
	return


S,f = string2freq('Hello')
n = len(S)
print(f)





bh = huffmanEncode()
#bh.buildHeap(f)
for i in range(1, n):
	bh.insert(f[i])
	bh.percUp
#print(bh)
#for k=n+1 to 2n-1:


print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
#print(bh.delMin())
#print(bh.delMin())





#http://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html
#string2freq('Hello my name is Inigo Montoya, you killed my father. Prepare to die.')