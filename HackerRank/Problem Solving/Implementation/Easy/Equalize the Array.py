n = int(input())
arr = list(map(int, input().split()))
dic = {0: 0}
for x in arr:
	if x in dic.keys():
		dic[x] += 1
	else:
		dic[x] = 1
high = 0
for x in dic.keys():
	if dic[x] > dic[high]:
		high = x
print(n - dic[high])
