s = input()
l = int(input())
a = []
for i in range(0, len(s), l):
	j = i + l
	x = s[i:j]
	a.append(list(x))
print(*list("".join(dict.fromkeys(x)) for x in a), sep="\n")
