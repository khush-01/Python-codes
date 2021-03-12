from math import ceil


for _ in range(int(input())):
	n, b, m = map(int, input().split())
	time = 0
	while n:
		time += ceil(n / 2) * m
		n //= 2
		m *= 2
		if n:
			time += b
	print(time)
