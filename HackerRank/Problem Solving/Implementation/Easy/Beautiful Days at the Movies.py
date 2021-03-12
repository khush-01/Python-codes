i, j, k = map(int, input().split())
count = 0
for x in range(i, j+1):
	num = x - int(str(x)[::-1])
	if num % k == 0:
		count += 1
print(count)
