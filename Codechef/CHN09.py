for _ in range(int(input())):
	cnt = {'a': 0, 'b': 0}
	s = input()
	for x in s:
		cnt[x] += 1
	print(min(cnt.values()))
