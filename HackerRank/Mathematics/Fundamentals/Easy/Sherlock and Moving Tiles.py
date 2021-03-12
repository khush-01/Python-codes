from math import sqrt


l, s1, s2 = map(int, input().split())
q = int(input())
dis = abs(s1 - s2)
for _ in range(q):
	x = int(input())
	a = sqrt(2) * (l - sqrt(x))
	t = a / dis 
	print("{:.20f}".format(t))
