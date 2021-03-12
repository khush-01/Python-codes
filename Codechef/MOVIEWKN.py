for _ in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))
	r = list(map(int, input().split()))
	mxm = 0
	pdt = 0
	for x in range(n):
		if l[x] * r[x] > pdt:
			pdt = l[x] * r[x]
			mxm = x
		elif l[x] * r[x] == pdt:
			if r[x] > r[mxm]:
				mxm = x
			elif r[x] == r[mxm]:
				mxm = min(mxm, x)
			else:
				pass
		else:
			pass
	print(mxm + 1)
