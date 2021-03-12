for _ in range(int(input())):
	n = int(input())
	s = list(input())
	u = list(input())
	cnt = 0
	i = 0
	while i < n:
		if u[i] == 'N':
			i += 1
		elif u[i] == s[i]:
			cnt += 1
			i += 1
		else:
			i += 2
	print(cnt)
