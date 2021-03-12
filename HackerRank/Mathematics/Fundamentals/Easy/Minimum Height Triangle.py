b, a = map(int, input().split())
h = 2 * a / b
if h - int(h) == 0:
	print(int(h))
else:
	print(int(h) + 1)
