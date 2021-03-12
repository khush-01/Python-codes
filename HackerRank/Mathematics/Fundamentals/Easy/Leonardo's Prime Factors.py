prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47] #, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for _ in range(int(input())):
	n = int(input())
	pdt = 1
	count = 0
	for x in prime:
		pdt *= x
		if pdt > n:
			break
		elif pdt == n:
			count += 1
			break
		count += 1
	print(count)
