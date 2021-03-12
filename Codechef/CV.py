for _ in range(int(input())):
	n = int(input())
	s = input()
	cnt = 0
	for x in range(n-1):
		if s[x] in "bcdfghjklmnpqrstvwxyz" and s[x+1] in "aeiou":
			cnt += 1
	print(cnt)
