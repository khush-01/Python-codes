a = [list(map(int, input().split())) for _ in range(6)]
sums = []
for x in range(4):
	for y in range(4):
		tot = a[x][y] + a[x][y+1] + a[x][y+2] + a[x+1][y+1] + a[x+2][y] + a[x+2][y+1] + a[x+2][y+2]
		sums.append(tot)
print(max(sums))
