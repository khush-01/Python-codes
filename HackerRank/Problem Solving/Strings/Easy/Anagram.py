for _ in range(int(input())):
	s = input()
	count = -1
	if len(s) % 2:
		print(count)
	else:
		count += 1
		s1 = list(s[:len(s)//2])
		s2 = list(s[len(s)//2:])
		s1.sort()
		s2.sort()
		for x in s2:
			if x not in s1:
				count += 1
		print(count)
