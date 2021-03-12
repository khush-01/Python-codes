n, d = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
dic = {}
for x in arr:
	if x in dic.keys():
		dic[x] += 1
	else:
		dic[x] = 1
for x in arr[::-1]:
	num1 = x - d
	num2 = num1 - d
	if num1 in arr and num2 in arr:
		count += 1 * dic[num1] * dic[num2]
print(count)
