n = int(input())
arr = list(map(int, input().split()))
val = arr[-1]
i = n-2
while i >= 0:
	if arr[i] > val:
		arr[i+1] = arr[i]
	else:
		arr[i+1] = val
		break
	i -= 1
	print(*arr)
if val < arr[0]:
	arr[0] = val
print(*arr)
