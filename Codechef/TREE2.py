for _ in range(int(input())):
	n = int(input())
	l = set(map(int, input().split()))
	l.discard(0)
	print(len(l))
