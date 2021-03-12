for _ in range(int(input())):
	q, p = map(int, input().split())
	if q > 1000:
		cost = 0.9 * q * p
	else:
		cost = q * p
	print("{:.6f}".format(cost))
