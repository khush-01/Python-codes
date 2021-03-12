for _ in range(int(input())):
	s1 = list(input().split())
	s2 = list(input().split())
	cnt = 0
	for x in s2:
		if x in s1:
			cnt += 1
	if cnt >= 2:
		print("similar")
	else:
		print("dissimilar")
