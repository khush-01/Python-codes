arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
a, b = 0, 0
for x in range(3):
	if arr1[x] > arr2[x]:
		a += 1
	elif arr1[x] < arr2[x]:
		b += 1
print(a, b)
