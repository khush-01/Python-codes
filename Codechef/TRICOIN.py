from math import sqrt


for _ in range(int(input())):
	c = int(input())
	d = 1 + 8 * c
	x = int((sqrt(d) - 1) // 2)
	print(x)
