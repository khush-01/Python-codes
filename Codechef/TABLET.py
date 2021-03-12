for _ in range(int(input())):
	n, b = map(int, input().split())
	a = [list(map(int, input().split())) for _ in range(n)]
	a.sort(key = lambda x: x[2])

	maxm = -float('inf')
	for x in a:
		if x[2] <= b:
			maxm = max(maxm, x[0]*x[1])
		else:
			break
	if maxm != -float('inf'):
		print(maxm)
	else:
		print("no tablet")
