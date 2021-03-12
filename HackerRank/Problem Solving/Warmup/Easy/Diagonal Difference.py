num = int(input())
arr = []
for i in range(num):
	arr.append(list(map(int, input().split())))
d1 = 0
d2 = 0
for i in range(num):
	for j in range(num):
		if i == j and i == (num//2) and num % 2:
			d1 += arr[i][j]
			d2 += arr[i][j]
		elif i == j:
			d1 += arr[i][j]
		elif i + j == (num - 1):
			d2 += arr[i][j]
print(abs(d1 - d2))
