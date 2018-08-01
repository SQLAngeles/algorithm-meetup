class Stack(object):
	
	def __init__(self):
		self.stack = []

	def push(self, val):
		self.stack.append(val)

	def pop(self):
		if not self.is_empty():
			self.stack.pop()
		else:
			print("underflow")

	def is_empty(self):
		return False if self.stack else True

	def travel(self):
		print(self.stack)

q = Stack()
q.push(1)
q.push(2)
q.travel()
q.pop()
q.push(3)
q.travel()
q.pop()
q.pop()
q.pop()
