for _ in range(int(input())):
	a, b, n = map(int, input().split())
	n %= 2
	a *= 2 ** n
	print(max(a, b) // min(a, b))
