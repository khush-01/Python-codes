from math import sqrt


for _ in range(int(input())):
	n = int(input())
	cnt = 0
	while n:
		cnt += 1
		tot = int(sqrt(n)) ** 2
		n -= tot
	print(cnt)
