from math import sqrt


def isprime(n):
	for x in range(int(sqrt(n)), 1, -1):
		if n % x == 0:
			return False
	return True


x = 1
primes = [0]
while x <= 2050:
	x += 1
	if isprime(x):
		primes.append(x)
	else:
		continue

for _ in range(int(input())):
	x, y = map(int, input().split())
	sm = x + y
	for i in range(len(primes)):
		if primes[i] <= sm:
			i += 1
		else:
			break
	print(primes[i] - sm)
