n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse = True)
if arr[0] <= k:
	print(0)
else:
	print(arr[0] - k)
