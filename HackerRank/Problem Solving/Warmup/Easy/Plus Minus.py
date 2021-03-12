n = int(input())
arr = list(map(int, input().split()))
count = [0, 0, 0]
for x in arr:
	if x > 0:
		count[0] += 1
	elif x < 0:
		count[1] += 1
	else:
		count[2] += 1
for x in count:
	print("{:.6f}".format(x/n))
