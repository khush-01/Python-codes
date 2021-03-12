for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	mxm = 0
	for i in range(n):
		score = a[i] * 20 - b[i] * 10
		mxm = max(mxm, score)
	print(mxm)
