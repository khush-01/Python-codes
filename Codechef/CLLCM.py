for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	flag = 1
	for x in a:
		if x % 2 == 0:
			flag = 0
			break
	if flag:
		print("YES")
	else:
		print("NO")
