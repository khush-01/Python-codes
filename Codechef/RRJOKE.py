for _ in range(int(input())):
	n = int(input())
	l = []
	for _ in range(n):
		l.append(input())
	r = n % 4
	if r == 0:
		print(n)
	elif r == 1:
		print(1)
	elif r == 2:
		print(n+1)
	else:
		print(0)
