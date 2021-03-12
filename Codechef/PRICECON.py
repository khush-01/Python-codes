for _ in range(int(input())):
	n, k = map(int, input().split())
	loss = 0
	arr = list(map(int, input().split()))
	for x in arr:
		if x > k:
			loss += x - k
	print(loss)
