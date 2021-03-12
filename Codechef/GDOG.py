for _ in range(int(input())):
	n, k = map(int, input().split())
	l = []
	for x in range(1, k+1):
		l.append(n%x)
	print(max(l))
