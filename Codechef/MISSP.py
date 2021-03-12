for _ in range(int(input())):
	n = int(input())
	l = set()
	for _ in range(n):
		x  = int(input())
		if x in l:
			l.remove(x)
		else:
			l.add(x)
	print(*l, sep = "\n")
