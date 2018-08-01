class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue(object):
	
	head = None
	tail = None

	def enqueue(self, val):
		if self.is_empty():
			self.head = Node(val)
			self.tail = self.head
		else:
			self.tail.next = Node(val)
			self.tail = self.tail.next

	def dequeue(self):
		if not self.is_empty():
			self.head = self.head.next
		else:
			print("underflow")
	def is_empty(self):
		return True if self.head is None else False

	def travel(self):
		t = self.head
		while t != None:
			print(t.val)
			t = t.next

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.travel()
q.dequeue()
q.enqueue(3)
q.travel()
q.dequeue()
q.dequeue()
q.dequeue()
