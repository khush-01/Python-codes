for _ in range(int(input())):
	a, b = map(int, input().split())
	p = 0
	i = 1
	while True:
		if a-i >= 0 and p == 0:
			a -= i
			p = 1
		else:
			break
		i += 1
		if b-i >= 0 and p == 1:
			b -= i
			p = 0
		else:
			break
		i += 1
	if p:
		print("Limak")
	else:
		print("Bob")
