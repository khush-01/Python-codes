for _ in range(int(input())):
	n = int(input())
	l = [1, 2]
	for i in range(2, n):
		l.append(0)
		l[i] = l[i-1] + 3
	for i in range(n):
		print(l[i], end=" ")
	print("")
