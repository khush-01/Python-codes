for _ in range(int(input())):
	n = int(input())
	s, r = input(), input()
	c1 = 0
	c2 = 0
	for x in s:
		if x == '1':
			c1 += 1
	for x in r:
		if x == '1':
			c2 += 1
	if c1 == c2:
		print("YES")
	else:
		print("NO")
