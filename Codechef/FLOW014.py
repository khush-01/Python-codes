for _ in range(int(input())):
	h, c, t = map(float, input().split())
	h = h > 50
	c = c < 0.7
	t = t > 5600
	if h and c and t:
		print(10)
	elif h and c:
		print(9)
	elif c and t:
		print(8)
	elif t and h:
		print(7)
	elif h or c or t:
		print(6)
	else:
		print(5)
