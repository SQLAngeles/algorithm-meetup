class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack(object):
	
	head = None

	def push(self, val):
		new = Node(val)
		new.next = self.head
		self.head = new

	def pop(self):
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
