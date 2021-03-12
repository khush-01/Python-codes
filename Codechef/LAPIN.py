for _ in range(int(input())):
	s = list(input())
	l = len(s)
	mid = l // 2
	s1 = sorted(s[:mid])
	if l % 2:
		s2 = sorted(s[mid+1:])
	else:
		s2 = sorted(s[mid:])
	if s1 == s2:
		print("YES")
	else:
		print("NO")
