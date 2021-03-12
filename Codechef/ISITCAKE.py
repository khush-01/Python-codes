for _ in range(int(input())):
	times = [list(map(int, input().split())) for _ in range(10)]
	cnt = 0
	for a in times:
		for x in a:
			if x <= 30:
				cnt += 1
	if cnt >= 60:
		print("yes")
	else:
		print("no")
