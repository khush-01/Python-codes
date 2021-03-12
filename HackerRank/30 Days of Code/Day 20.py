n = int(input())
a = list(map(int, input().split()))
tot = 0
for i in range(n):
	num = 0
	for j in range(n-i-1):
		if a[j] > a[j+1]:
			a[j], a[j+1] = a[j+1], a[j]
			num += 1
	if num == 0:
		break
	tot += num
print("Array is sorted in {} swaps.".format(tot))
print("First Element:", a[0])
print("Last Element:", a[n-1])
