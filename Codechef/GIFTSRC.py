for _ in range(int(input())):
	p = [0, 0]
	n = int(input())
	s = input()
	prev = s[0]
	if prev == "L":
		p[0] -= 1
	elif prev == "R":
		p[0] += 1
	elif prev == "U":
		p[1] += 1
	else:
		p[1] -= 1
	for x in s[1:]:
		if x == "L" and prev not in "LR":
			p[0] -= 1
		elif x == "R" and prev not in "LR":
			p[0] += 1
		elif x == "U" and prev not in "UD":
			p[1] += 1
		elif x == "D" and prev not in "UD":
			p[1] -= 1
		else:
			continue
		prev = x
	print(*p)
