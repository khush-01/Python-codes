n = int(input())
p = int(input())
arr = []
for i in range(0, n+1, 2):
	arr.append([i, i+1])
count = 0
if p > (n // 2):
	arr.reverse()
for x in arr:
	if p not in x:
		count += 1
	else:
		break
print(count)
