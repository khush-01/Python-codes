for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	max = 0
	min = 0
	for x in range(n):
		if a[max] < a[x]:
			max = x
		if a[min] > a[x]:
			min = x
	if max < min:
		print(a[max], a[min])
	else:
		print(a[min], a[max])
