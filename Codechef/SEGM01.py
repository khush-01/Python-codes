for _ in range(int(input())):
	s = input()
	s = s.lstrip('0').rstrip('0')
	if '0' not in s and len(s):
		print("YES")
	else:
		print("NO")
