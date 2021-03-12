for _ in range(int(input())):
	num = input()
	n = int(num)
	count = 0
	for x in num:
		if x == "0":
			continue
		else:
			if n % int(x) == 0:
				count += 1
	print(count)
