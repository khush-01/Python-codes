for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	prev = 0
	cnt = 0
	for i in range(n):
		if b[i] <= a[i] - prev:
			cnt += 1
		prev = a[i]
	print(cnt)
