n = int(input())
arr = list(map(int, input().split()))
count = 0
i = 0
while i < n:
	if i == n-1:
		break
	if i == n-2:
		count += 1
		break
	if arr[i+2] == 1:
		i += 1
	else:
		i += 2
	count += 1
print(count)
