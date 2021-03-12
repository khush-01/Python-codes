def count(arr):
	c = 0
	for x in arr:
		if x == 1:
			c += 1
	return c


n, k = map(int, input().split())
l = [0 for _ in range(n+1)]
for _ in range(k):
	line = input().split()
	if line[0] == "CLOSEALL":
		l = [0 for _ in range(n+1)]
	else:
		x = int(line[1])
		l[x] = (l[x] + 1) % 2
	print(count(l))
