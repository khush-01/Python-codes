arr = list(map(int, input().split()))
minsum = 0
maxsum = 0
arr.sort()
for i in range(5):
	if i == 0:
		minsum += arr[i]
	elif i == 4:
		maxsum += arr[i]
	else:
		minsum += arr[i]
		maxsum += arr[i]
print(minsum, maxsum)
