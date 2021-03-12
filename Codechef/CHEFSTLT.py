for _ in range(int(input())):
	a, b = input(), input()
	cq = 0
	cn = 0
	for x in range(len(a)):
		if a[x] == '?' or b[x] == '?':
			cq += 1
		elif a[x] != b[x]:
			cn += 1
		else:
			continue
	print(cn, cn+cq)
