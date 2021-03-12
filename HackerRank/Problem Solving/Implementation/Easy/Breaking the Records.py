n = int(input())
scores = list(map(int, input().split()))
countmin = 0
countmax = 0
low = scores[0]
high = scores[0]
for i in range(1, n):
	if scores[i] < low:
		low = scores[i]
		countmin += 1
	elif scores[i] > high:
		high = scores[i]
		countmax += 1
	else:
		continue
print(countmax, countmin)
