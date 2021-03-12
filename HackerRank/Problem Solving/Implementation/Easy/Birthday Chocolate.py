def arrsum(arr):
	sum = 0
	for x in arr:
		sum += x
	return sum

n = int(input())
choc = list(map(int, input().split()))
d, m = map(int, input().split())
bars = []
for i in range(m, n + 1):
	bars.append(choc[i-m:i])
count = 0
if n == 1:
	for x in choc:
		if x == d:
			count += 1
else:
	for x in bars:
		# print(x, arrsum(x))
		if arrsum(x) == d:
			count += 1
print(count)
