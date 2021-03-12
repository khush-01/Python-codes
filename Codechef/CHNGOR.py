for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	res = a[0]
	for x in a[1:]:
		res = res | x
	print(res)
