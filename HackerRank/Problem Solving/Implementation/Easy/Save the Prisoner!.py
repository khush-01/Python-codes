for _ in range(int(input())):
	n, m, s = map(int, input().split())
	out = ((m + s - 1) % n)
	if out == 0:
		print(n)
	else:
		print(out)
