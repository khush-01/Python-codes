for _ in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))
	print((n - 1) * min(l))