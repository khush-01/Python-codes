for _ in range(int(input())):
	n, k = map(int, input().split())
	arr = list(map(int, input().split()))
	count = 0
	for x in arr:
		if x <= 0:
			count += 1
	if count < k:
		print("YES")
	else:
		print("NO")
