mod = 10 ** 9 + 7

for _ in range(int(input())):
	n = int(input())
	print((n % mod) * (n % mod) % mod)
