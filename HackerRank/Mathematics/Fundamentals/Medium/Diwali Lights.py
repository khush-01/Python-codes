mod = 10 ** 5

def pow(x, n):
	if n == 0:
		return 1
	if n % 2 == 0:
		return pow((x*x) % mod, n//2) % mod
	else:
		return ((x % mod) * (pow((x*x) % mod, n//2) % mod)) % mod


for _ in range(int(input())):
	n = int(input())
	print(pow(2, n) - 1)
