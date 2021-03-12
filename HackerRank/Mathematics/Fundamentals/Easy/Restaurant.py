def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a%b)


for _ in range(int(input())):
	l, b = map(int, input().split())
	hcf = gcd(max(l, b), min(l, b))
	print((l // hcf) * (b // hcf))
