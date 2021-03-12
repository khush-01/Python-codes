def height(n):
	h = 1
	for i in range(1, n+1):
		if i % 2 == 0:
			h += 1
		else:
			h *= 2
	return h


for _ in range(int(input())):
	print(height(int(input())))
