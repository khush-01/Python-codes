from math import gcd

for _ in range(int(input())):
	n, m = map(int, input().split())
	x = gcd(n, m)
	print(n * m // x // x)
