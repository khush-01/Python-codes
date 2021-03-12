for _ in range(int(input())):
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	a.insert(0, 0)
	left = [0] * (n+1)
	flag = 0
	for i in range(1, n+1):
		if a[i] + left[i-1] < k:
			flag = i
			break
		else:
			left[i] = a[i] + left[i-1] - k
	if flag:
		print("NO", flag)
	else:
		print("YES")
