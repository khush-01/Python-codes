for _ in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))
	alt = [1]
	prev = l[-1]
	for x in l[-2::-1]:
		if x * prev < 0:
			alt.append(alt[-1] + 1)
		else:
			alt.append(1)
		prev = x
	print(*alt[::-1])
