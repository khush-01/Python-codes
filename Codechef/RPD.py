def digitsum(num):
	tot = 0
	for x in str(num):
		tot += int(x)
	return tot


for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	mxm = -float('inf')
	for i in range(n):
		for j in range(i+1, n):
			mxm = max(mxm, digitsum(a[i]*a[j]))
	print(mxm)
