for _ in range(int(input())):
	n = int(input())
	s = input()
	a = {'R': 0, 'G': 0, 'B': 0}
	for x in s:
		a[x] += 1
	print(n - max(a.values()))
