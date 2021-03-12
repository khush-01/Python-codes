for _ in range(int(input())):
	n = int(input())
	a = [[0 for _ in range(n)] for _ in range(n)]
	p = 1
	for k in range(n):
		j = k
		i = 0
		while j >= 0:
			a[i][j] = p
			p += 1
			i += 1
			j -= 1
	for k in range(1, n):
		i = k
		j = n - 1
		while j >= k:
			a[i][j] = p
			p += 1
			i += 1
			j -= 1
	for x in a:
		print(*x)
