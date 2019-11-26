class Queue:
	def __init__(self):
		self._queue = []

	def add(self, element):
		self._queue.append(element)

	def pop(self):
		self._queue.pop(0)

	def remove(self, element):
		return self._queue.remove(element)

	def __contains__(self, element):
		return element in self._queue

	def clear(self):
		self._queue.clear()

	def size(self):
		return len(self._queue)

	def __iter__(self):
		return self._queue.__iter__()

class FrameQueue:
	def __init__(self, size):
		self._queue = Queue()
		self._size = size
		self._pageFaults = 0

	def _isMax_(self):
		return self._queue.size() == self._size

	def _incPF_(self):
		self._pageFaults += 1

	def lru(self, l):
		self.clear()
		for element in l:
			self.lruE(element)
			print(element, self._queue._queue)

	def lruE(self, element):
		if element in self._queue:
			self._queue.remove(element)
		else:
			if self._isMax_():
				self._queue.pop()
			self._incPF_()

		self._queue.add(element)

	def fifo(self, l):
		self.clear()
		for element in l:
			self.fifoE(element)
			print(element, self._queue._queue)

	def fifoE(self, element):
		if element not in self._queue:
			if self._isMax_():
				self._queue.pop()

			self._queue.add(element)
			self._incPF_()

	def clear(self):
		self._queue.clear()
		self._pageFaults = 0

	def getPF(self):
		return self._pageFaults

	def getQ(self):
		return self._queue._queue

	def getSize(self):
		return self._size

	def __str__(self):
		l = ""

		for element in self._queue:
			l += str(element) + " "

		return l