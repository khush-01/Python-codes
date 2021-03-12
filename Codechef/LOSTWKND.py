for _ in range(int(input())):
	a = list(map(int, input().split()))
	p = a.pop(-1)
	if sum(a) * p > 120:
		print("Yes")
	else:
		print("No")
