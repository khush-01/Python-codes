from math import sqrt, floor, ceil


for _ in range(int(input())):
	a, b = map(int, input().split())
	n1 = ceil(sqrt(a))
	n2 = floor(sqrt(b))
	print(n2 - n1 + 1)
