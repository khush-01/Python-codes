for _ in range(int(input())):
	s = input()
	if s == s[::-1]:
		print("wins")
	else:
		print("loses")
