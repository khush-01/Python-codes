for _ in range(int(input())):
	n = int(input()) // 4
	a = list(map(int ,input().split()))
	a.sort()
	x = n
	y = 2 * n
	z = 3 * n
	if a[x] == a[x-1] or a[y] == a[y-1] or a[z] == a[z-1]:
		print(-1)
	else:
		print(a[x], a[y], a[z])
