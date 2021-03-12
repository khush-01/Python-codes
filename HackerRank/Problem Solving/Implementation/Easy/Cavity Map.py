n = int(input())
a = [input() for _ in range(n)]
for x in range(0, n):
	for y in range(0, n):
		if x == 0 or y == 0 or x + 1 == n or y + 1 == n:
			print(a[x][y], end="")
		elif a[x][y] > max(a[x-1][y], a[x][y-1], a[x][y+1], a[x+1][y]):
			print('X', end="")
		else:
			print(a[x][y], end="")
	print("")
