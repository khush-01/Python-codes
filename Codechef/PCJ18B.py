for  _ in range(int(input())):
	n = int(input())
	tot = 0
	for i in range(1, n+1, 2):
		tot += (n-i+1) ** 2
	print(tot)
