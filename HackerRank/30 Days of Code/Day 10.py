n = bin(int(input()))[2:]
a = []
cnt = 0
for x in n:
	if x == '1':
		cnt += 1
	else:
		a.append(cnt)
		cnt = 0
	a.append(cnt)
print(max(a))
