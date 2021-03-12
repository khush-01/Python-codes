for _ in range(int(input())):
	n = int(input())
	s = input()
	count = {}
	for x in s:
		if x in count.keys():
			count[x] += 1
		else:
			count[x] = 1
	flag = 1
	for x in count.keys():
		if x == "_":
			continue
		if count[x] == 1:
			flag = 0
			break
	if flag:
		print("YES")
	else:
		print("NO")
