from math import sqrt


for _ in range(int(input())):
	n = int(input())
	cnt = 0
	if n % 2 == 0:
		for x in range(1, int(sqrt(n))+1):
			if n % x == 0 and x % 2 == 0:
				cnt += 1
			if n % (n // x) == 0 and (n // x) % 2 == 0:
				cnt += 1
			if x == n // x and x % 2 == 0 and n % x == 0:
				cnt -= 1
	print(cnt)
