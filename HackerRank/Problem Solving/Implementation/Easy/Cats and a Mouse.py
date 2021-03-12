for _ in range(int(input())):
	x, y, z = map(int, input().split())
	a = abs(z - x)
	b = abs(z - y)
	if a < b:
		print("Cat A")
	elif b < a:
		print("Cat B")
	else:
		print("Mouse C")
