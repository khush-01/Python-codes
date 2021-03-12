for _ in range(int(input())):
	n, x = map(int, input().split())
	a = {x}
	s = input()
	for y in s:
		if y == "R":
			x += 1
		else:
			x -= 1
		a.add(x)
	print(len(a))
