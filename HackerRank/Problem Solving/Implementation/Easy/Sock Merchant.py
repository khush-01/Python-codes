socks = {}
n = int(input())
arr = list(map(int, input().split()))
for x in arr:
	if x in socks.keys():
		socks[x] += 1
	else:
		socks[x] = 1
count = 0
for x in socks.values():
	count += x // 2
print(count)
