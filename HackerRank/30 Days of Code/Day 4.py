class Person(object):
	def __init__(self, age):
		if age < 0:
			print("Age is not valid, setting age to 0.")
			self.age = 0
		else:
			self.age = age

	def yearPasses(self):
		self.age += 1

	def amIOld(self):
		if self.age < 13:
			print("You are young.")
		elif 13 <= self.age < 18:
			print("You are a teenager.")
		else:
			print("You are old.")


for _ in range(int(input())):
	age = int(input())
	p = Person(age)
	p.amIOld()
	for _ in range(3):
		p.yearPasses()
	p.amIOld()
	print("")
