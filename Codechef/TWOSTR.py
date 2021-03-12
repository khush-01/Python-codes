for _ in range(int(input())):
	a = input()
	b = input()
	flag = 1
	for x in range(len(a)):
		if a[x] != b[x]:
			if a[x] != '?' and b[x] != '?' :
				flag = 0
				break
	if flag:
		print("Yes")
	else:
		print("No")
