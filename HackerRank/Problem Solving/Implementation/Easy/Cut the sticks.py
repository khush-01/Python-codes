n = int(input())
arr = list(map(int, input().split()))
while len(arr):
	print(len(arr))
	low = min(arr)
	arr = [x for x in arr if x != low]
	for x in arr:
		x -= low
