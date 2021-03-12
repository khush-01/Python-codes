for _ in range(int(input())):
	r = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	c = list(map(int, input().split()))

	d1 = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
	d2 = (b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2
	d3 = (c[0] - a[0]) ** 2 + (c[1] - a[1]) ** 2

	p1 = d1 <= r * r 
	p2 = d2 <= r * r
	p3 = d3 <= r * r

	if p1 and p2 or p2 and p3 or p3 and p1:
		print("yes")
	else:
		print("no")
