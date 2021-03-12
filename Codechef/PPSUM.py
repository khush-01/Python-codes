for _ in range(int(input())):
	d, n = map(int, input().split())
	tot = 0
	while d:
		tot = n * (n + 1) // 2
		n = tot 
		d -= 1
	print(tot)
