n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
a.insert(0, 0)
a.append(n-1)
left = a[1] - a[0]
right = a[-1] - a[-2]
d = 0
prev = a[1]
for x in a[2:-1]:
	d = max(x-prev, d)
	prev = x
print(max(left, right, d//2))
