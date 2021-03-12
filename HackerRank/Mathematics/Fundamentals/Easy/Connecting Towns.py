mod = 1234567

for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	pdt = 1
	for x in arr:
		pdt = ((pdt % mod) * x) % mod
	print(pdt)
