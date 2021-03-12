s = list(input())
for _ in range(int(input())):
	w = sorted(list(set(input())))
	for x in w:
		if x not in s:
			print("No")
			break
	else:
		print("Yes")
