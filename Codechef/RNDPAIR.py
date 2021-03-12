for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	cnt = {}
	for x in a:
		if x in cnt.keys():
			cnt[x] += 1
		else:
			cnt[x] = 1
	tot = n * (n - 1) // 2
	mxm1 = max(cnt.keys())
	mx1 = cnt[mxm1]
	cnt[mxm1] -= 1
	if cnt[mxm1] == 0:
		del cnt[mxm1]
	mxm2 = max(cnt.keys())
	mx2 = cnt[mxm2]
	odds = mx1 * mx2
	if mxm1 == mxm2:
		odds /= 2
	prob = odds / tot
	print("{:.8f}".format(prob))
