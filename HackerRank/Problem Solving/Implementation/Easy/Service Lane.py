n, t = map(int, input().split())
arr = list(map(int, input().split()))
test = []
for _ in range(t):
	test.append(list(map(int, input().split())))
for x in test:
	print(min(arr[x[0]:x[1]+1]))
