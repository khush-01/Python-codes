for _ in range(int(input())):
	p1, p2, k = map(int, input().split())
	turn = (p1 + p2) // k
	if turn % 2 == 0:
		print("Chef")
	else:
		print("Paja")
