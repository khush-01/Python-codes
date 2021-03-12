from math import ceil


r, c = map(int, input().split())
col = [[0, 0, 2, 4, 6, 8], [0, 1, 3, 5, 7, 9]]
num = 0
if r % 2 == 0:
	num += col[1][c]
else:
	num += col[0][c]
row = ceil(r / 2)
num += (10 * (row - 1))
print(num)
