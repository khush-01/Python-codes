for _ in range(int(input())):
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	flag = 0
	for x in a:
		if x >= k:
			flag = 1
			break
	if flag:
		print("YES")
	else:
		print("NO")
