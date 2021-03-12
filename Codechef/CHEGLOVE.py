for _ in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))
	g = list(map(int, input().split()))
	front = 0
	back = 0
	for x in range(n):
		if l[x] <= g[x]:
			front = 1
		else:
			front = 0
			break
	g = g[::-1]
	for x in range(n):
		if l[x] <= g[x]:
			back = 1
		else:
			back = 0
			break
	if front:
		if back:
			print("both")
		else:
			print("front")
	else:
		if back:
			print("back")
		else:
			print("none")
