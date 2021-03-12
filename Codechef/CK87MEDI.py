for _ in range(int(input())):
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	a.sort()
	mid = (n + k) // 2
	print(a[mid])
