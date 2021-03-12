for _ in range(int(input())):
	a = [list(input()) for _ in range(3)]
	flag = 0
	for i in range(2):
		for j in range(2):
			if a[i][j] == 'l':
				if a[i+1][j] == 'l' and a[i+1][j+1] == 'l':
					flag = 1
					break
		if flag:
			break
	if flag:
		print("yes")
	else:
		print("no")
