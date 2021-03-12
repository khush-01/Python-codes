p, d, m, s = map(int, input().split())
count = 0
total = 0
while total <= s:
	if total + p > s:
		break
	else:
		total += p
	p -= d
	if p <= m:
		p = m
		d = 0
	count += 1
print(count)
