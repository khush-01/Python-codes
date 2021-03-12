cnt = [0]
mon = [1, 2, 5, 10, 50, 100]
for i in range(1, 1000001):
	cnt.append(float('inf'))
	for x in mon:
		if i >= x:
			cnt[i] = min(cnt[i], cnt[i-x]+1)
for _ in range(int(input())):
	print(cnt[int(input())])
