for _ in range(int(input())):
	n, c, m = map(int, input().split())
	choc = n // c
	count = choc
	while True:
		count += choc // m
		if choc // m == 0:
			break
		else:
			choc = choc // m + choc % m
	print(count)
