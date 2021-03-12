l = []
for _ in range(int(input())):
	l.append(int(input()))
print(*sorted(l), sep="\n")
