for _ in range(int(input())):
	n, k = map(int, input().split())
	a = [list(map(int, input().split())) for _ in range(n)]
	cost = 0
	tot = 0
	for x in a:
		if tot + x[0] > k:
			tot += x[0]
			cost += (tot - k) * x[1]
		elif tot > k:
			tot += x[0]
			cost += x[0] * x[1]
		else:
			tot += x[0]
	print(cost)
