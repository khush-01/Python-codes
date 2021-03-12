for _ in range(int(input())):
	c, d, l = map(int, input().split())
	if l % 4:
		print("no")
	else:
		g = c + d - l // 4
		if 0 <= g <= min(c, 2 * d):
			print("yes")
		else:
			print("no")
