for _ in range(int(input())):
	s = input()
	c0 = 0
	c1 = 0
	for x in s:
		if x == '0':
			c0 += 1
		else:
			c1 += 1
	if c0 == 1 or c1 == 1 and c0 != c1:
		print("Yes")
	else:
		print("No")
