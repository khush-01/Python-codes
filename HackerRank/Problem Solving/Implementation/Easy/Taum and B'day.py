for _ in range(int(input())):
	b, w = map(int, input().split())
	bc, wc, z = map(int, input().split())
	if z >= abs(bc - wc):
		cost = b * bc + w * wc
	else:
		if bc > wc:
			cost = (w + b) * wc + b * z
		else:
			cost = (w + b) * bc + w * z
	print(cost)
