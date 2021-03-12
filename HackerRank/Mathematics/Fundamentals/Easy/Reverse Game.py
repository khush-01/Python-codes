for _ in range(int(input())):
	n, k = map(int, input().split())
	if k < n // 2:
		print(2 * k + 1)
	else:
		print((n - 1 - k) * 2)
