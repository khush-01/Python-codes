for _ in range(int(input())):
	n, m, k = map(int, input().split())
	print(0 if k >= abs(n-m) else (max(n, m) - min(n, m) - k))
