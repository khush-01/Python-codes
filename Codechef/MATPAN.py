for _ in range(int(input())):
	a = list(map(int, input().split()))
	s = input()
	has = [False] * 26
	cost = 0
	for x in s:
		i = ord(x) - ord('a')
		if has[i] != True:
			has[i] = True
	for x in range(26):
		if has[x] != True:
			cost += a[x]
	print(cost)
