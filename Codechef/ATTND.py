for _ in range(int(input())):
	n = int(input())
	names = [list(map(str, input().split())) for _ in range(n)]
	first = [x[0] for x in names[1:]]
	full = []
	for i in range(n):
		x = names[i]
		if x[0] in first[i:] or  x[0] in full:
			full.append(x[0])
			print(*x)
		else:
			print(x[0])
