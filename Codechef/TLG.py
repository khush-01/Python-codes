n = int(input())
a, b = map(int, input().split())
sa = [a]
sb = [b]
for _ in range(n-1):
	a, b = map(int, input().split())
	sa.append(sa[-1]+a)
	sb.append(sb[-1]+b)
l = []
for x in range(n):
	l.append(sa[x]-sb[x])
l = sorted(l)
if -l[0] > l[-1]:
	print(2, -l[0])
else:
	print(1, l[-1])
