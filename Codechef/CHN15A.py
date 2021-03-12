for _ in range(int(input())):
	n, k = map(int, input().split())
	a = [int(x) + k for x in input().split()]
	cnt = 0
	for x in a:
		if x % 7 == 0:
			cnt += 1
	print(cnt)
