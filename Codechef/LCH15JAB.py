for _ in range(int(input())):
	s = input()
	cnt = {}
	for x in s:
		if x in cnt.keys():
			cnt[x] += 1
		else:
			cnt[x] = 1
	mxm = max(cnt.values())
	if mxm == len(s) - mxm:
		print("YES")
	else:
		print("NO")
