class Node(object):

	'''节点类'''
	def __init__(self, item):
		'''
		初始化函数
		:param item: 要保存的数据
		'''
		self.item = item
		self._next = None

class SignleCycleLinkedList(object):

	'''单向循环链表'''
	def __init__(self, node=None):
		'''
		初始化函数
		:param node: 头节点
		'''
		self._head = node

	def is_empty(self):
		return self._head is None

	def length(self):
		if self.is_empty():
			return 0

		current = self._head
		count = 1
		while current._next != self._head:
			count += 1
			current = current._next
		return count

	def travel(self):
		if self.is_empty():
			print('')
		current = self._head
		while current._next != self._head:
			print(current.item, end=' ')
			current = current._next
		print(current.item, end=' ')

	def add(self, item):
		node = Node(item)
		if self.is_empty():
			node._next = node
			self._head = node
		else:
			cur = self._head
			while cur._next != self._head:
				cur = cur._next
			node._next = self._head
			self._head = node
			cur._next = node

	def append(self, item):
		node = Node(item)
		if self.is_empty():
			self._head = node
			node._next = node
		else:
			cur = self._head
			while cur._next != self._head:
				cur = cur._next
			node._next = self._head
			cur._next = node

	def insert(self, pos, item):
		if pos <= 0:
			self.add(item)
		elif pos >= self.length():
			self.append(item)
		else:
			cur = self._head
			count = 0
			while count < (pos - 1):
