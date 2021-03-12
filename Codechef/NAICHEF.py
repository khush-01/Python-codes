for _ in range(int(input())):
	n, a, b = map(int, input().split())
	l = list(map(int, input().split()))
	cnt = {}
	for x in l:
		if x in cnt.keys():
			cnt[x] += 1
		else:
			cnt[x] = 1
	prob = (cnt[a] / n) * (cnt[b] / n)
	print("{:.10f}".format(prob))
