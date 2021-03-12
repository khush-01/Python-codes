for _ in range(int(input())):
	s = input()
	odd = ""
	even = ""
	for x in range(len(s)):
		if x % 2 == 0:
			even += s[x]
		else:
			odd += s[x]
	print(even, odd)
