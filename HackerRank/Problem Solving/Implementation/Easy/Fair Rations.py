n = int(input())
a = list(map(int, input().split()))
if sum(a) % 2:
	print("NO")
else:
	cnt = 0
	prev = -1
	for x in range(n):
		if a[x] % 2:
			if prev == -1:
				prev = x
			else:
				cnt += (x - prev) * 2
				prev = -1
	print(cnt)
