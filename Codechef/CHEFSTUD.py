for _ in range(int(input())):
	s = input()
	cnt = 0
	for x in range(len(s)-1):
		if s[x:x+2] == '<>':
			cnt += 1
	print(cnt)
