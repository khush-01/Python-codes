cnt = 0
for _ in range(int(input())):
	s = input()
	l = len(s)-1
	for i in range(l):
		x = s[i:i+2]
		if x in "chef":
			cnt += 1
			break
print(cnt)
