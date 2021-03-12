class Stack():
	def __init__(self):
		self.stack = []

	def pushCharacter(self, val):
		self.stack.append(val)

	def popCharacter(self):
		return self.stack.pop()

	def notEmpty(self):
		return len(self.stack) != 0


class Queue():
	def __init__(self):
		self.queue = []

	def enqueueCharacter(self, val):
		self.queue.append(val)

	def dequeueCharacter(self):
		return self.queue.pop(0)

	def notEmpty(self):
		return len(self.queue) != 0


stk = Stack()
que = Queue()
s = input()
for x in s:
	stk.pushCharacter(x)
	que.enqueueCharacter(x)
flag = 1
while stk.notEmpty() and que.notEmpty():
	if stk.popCharacter() != que.dequeueCharacter():
		flag = 0
		break
if flag:
	print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")
