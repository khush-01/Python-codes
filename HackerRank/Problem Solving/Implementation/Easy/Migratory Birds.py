n = int(input())
arr = list(map(int, input().split()))
count = [0] * 5
for x in arr:
	count[x-1] += 1
# print(count)
high = 0
for x in range(5):
	if count[x] > count[high]:
		high = x
print(high + 1)
