from math import sqrt

def isprime(n):
	if n == 1:
		return False
	if n != 2 and n % 2 == 0:
		return False
	for i in range(3, int(sqrt(n))+1, 2):
		if n % i == 0:
			return False
	return True

for _ in range(int(input())):
	if isprime(int(input())):
		print("Prime")
	else:
		print("Not prime")
