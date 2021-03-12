for _ in range(int(input())):
	px, py, qx, qy = map(int, input().split())
	x = 2 * qx - px
	y = 2 * qy - py
	print(x, y)
