def conv(num):
	cnt = 0
	for x in bin(num):
		if x == '1':
			cnt += 1
	return cnt


n, m = map(int, input().split())
arr = []
for _ in range(n):
	arr.append(int(input(), 2))
dic = {}
for i in range(n):
	for j in range(i+1, n):
		topics = conv(arr[i] | arr[j])
		if topics in dic.keys():
			dic[topics] += 1
		else:
			dic[topics] = 1
out = max(dic.keys())
print(out, dic[out], sep = "\n")
