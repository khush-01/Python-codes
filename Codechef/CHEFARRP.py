def apdt(arr):
	pdt = 1
	for x in arr:
		pdt *= x
	return pdt


for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	sub = [a[i:j] for i in range(n) for j in range(i+1, n+1)]
	cnt = 0
	for x in sub:
		if sum(x) == apdt(x):
			cnt += 1
	print(cnt)
