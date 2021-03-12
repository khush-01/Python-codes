def count(num):
	num = bin(num)
	cnt = 0
	for x in num:
		if x == '1':
			cnt += 1
	return cnt


for _ in range(int(input())):
	n = int(input())
	a = [int(input(), 2) for _ in range(n)]
	res = a[0]
	for x in a[1:]:
		res = res ^ x
	print(count(res))
