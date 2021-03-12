for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	b = []
	a.sort()
	for x in a:
		cnt = a[::-1].index(x)
		b.append(cnt)
	print(*b)
