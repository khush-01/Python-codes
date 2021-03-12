def sum(n):
	s = str(n)
	sum = 0
	for x in s:
		sum += int(x)
	return sum


def bestdiv(arr):
	best = 100000
	bsum = 1
	for x in arr:
		add = sum(x)
		if add > bsum:
			best = x
			bsum = add
		elif add == bsum:
			best = min(best, x)
			bsum = add
	return best


num = int(input())
factors = []
for i in range(1, num+1):
	if num % i == 0:
		factors.append(i)
print(bestdiv(factors))
