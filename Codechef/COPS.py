for _ in range(int(input())):
	m, x, y = map(int, input().split())
	a = list(map(int, input().split()))
	cover = x * y
	b = [[i-cover, i+cover] for i in a]
	c = set(i for i in range(1, 101))
	for i in b:
		for j in range(i[0], i[1]+1):
			try:
				c.remove(j)
			except KeyError:
				pass
	print(len(c))
