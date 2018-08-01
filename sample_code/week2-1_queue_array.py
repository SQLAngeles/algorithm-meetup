class Queue(object):
	
	def __init__(self):
		self.queue = []

	def enqueue(self, val):
		self.queue.insert(0, val)

	def dequeue(self):
		if not self.is_empty():
			self.queue.pop()
		else:
			print("underflow")

	def is_empty(self):
		return False if self.queue else True

	def travel(self):
		print(self.queue[-1::-1])

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
