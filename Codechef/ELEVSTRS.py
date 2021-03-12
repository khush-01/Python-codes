from math import sqrt


for _ in range(int(input())):
	n, v1, v2 = map(int, input().split())
	t1 = sqrt(2) * n / v1
	t2 = 2 * n / v2
	if t1 < t2:
		print("Stairs")
	else:
		print("Elevator")
