for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	s1 = sum(a) - max(a)
	s2 = sum(b) - max(b)
	if s1 < s2:
		print("Alice")
	elif s2 < s1:
		print("Bob")
	else:
		print("Draw")
