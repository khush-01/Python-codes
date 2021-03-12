for _ in range(int(input())):
	cnt = {}
	n = int(input())
	s = input()
	for x in s:
		if x in cnt.keys():
			cnt[x] += 1
		else:
			cnt[x] = 1
	flag = 1
	for x in cnt.values():
		if x % 2:
			flag = 0
			break
	if flag:
		print("YES")
	else:
		print("NO")
