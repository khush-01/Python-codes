for _ in range(int(input())):
	s = input()
	flag = 1
	for i in range(0, len(s)-1, 2):
		x = s[i:i+2]
		if x == "AB" or x == "BA":
			continue
		else:
			flag = 0
			break
	if flag:
		print("yes")
	else:
		print("no")
