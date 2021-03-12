for _ in range(int(input())):
	s = list(input())
	cnt = 0
	for i in range(len(s)-1):
		if s[i] != s[i+1]:
			cnt += 1
	if s[0] != s[-1]:
		cnt += 1
	if cnt <= 2:
		print("uniform")
	else:
		print("non-uniform")
