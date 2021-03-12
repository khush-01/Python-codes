for _ in range(int(input())):
	n = int(input())
	time = [list(map(int, input().split())) for _ in range(n)]
	cnt = 0
	for x in time:
		if x[1] - x[0] > 5:
			cnt += 1
	print(cnt)
