from math import gcd

for _ in range(int(input())):
	a, b = map(int, input().split())
	print(gcd(a, b), a * b // gcd(a, b))
