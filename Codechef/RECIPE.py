from math import gcd

def findgcd(l):
	res = gcd(l[1], l[2])
	for x in range(3, l[0]+1):
		res = gcd(res, l[x])
	return res


for _ in range(int(input())):
	arr = list(map(int, input().split()))
	hcf = findgcd(arr)
	for x in range(1, arr[0]+1):
		print(arr[x] // hcf, end=" ")
	print()
