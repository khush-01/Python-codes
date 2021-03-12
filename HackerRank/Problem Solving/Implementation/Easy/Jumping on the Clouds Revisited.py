n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
i = 0
while True:
	count += 1
	if arr[i] == 1:
		count += 2
	i = (i + k) % n
	if i == 0:
		break
print(100 - count)
