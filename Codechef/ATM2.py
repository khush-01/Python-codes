for _ in range(int(input())):
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	out = ""
	for x in a:
		if k >= x:
			out += '1'
			k -= x
		else:
			out += '0'
	print(out)
