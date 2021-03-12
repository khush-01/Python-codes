a = set(map(int, input().split()))
l = []
for _ in range(int(input())):
	l.append(set(map(int, input().split())))
flag = True
for x in l:
	if x.union(a) != a:
		flag = False
		break
print(flag)
