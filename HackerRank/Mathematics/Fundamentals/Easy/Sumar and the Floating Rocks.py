from math import gcd

for _ in range(int(input())):
	x1, y1, x2, y2 = map(int, input().split())
	y, x = abs(y2 - y1), abs(x2 - x1)
	print(gcd(x, y) - 1)
