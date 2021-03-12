def doublesearch(arr, num):
	i = 0
	for x in range(1, len(arr)+1):
		if arr[x-1] == num:
			i = x
			break
	num = i
	for x in range(1, len(arr)+1):
		if arr[x-1] == num:
			return x


n = int(input())
array = list(map(int, input().split()))
for x in range(1, n+1):
	print(doublesearch(array, x))
