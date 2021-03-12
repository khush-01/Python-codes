for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	m = int(input())
	b = list(map(int, input().split()))
	l = [0]
	flag = 1
	for x in b:
		try:
			l.append(a[l[-1]:].index(x))
		except:
			break
	if len(l) == m + 1:
		print("Yes")
	else:
		print("No")
