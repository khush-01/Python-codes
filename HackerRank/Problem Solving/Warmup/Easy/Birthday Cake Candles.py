num = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse = True)
count = 0
height = arr[0]
for x in arr:
	if x == height:
		count += 1
	else:
		break
print(count)
