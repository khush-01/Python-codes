def format(n):
	l = len(bin(n)[2:])
	arr = []
	for i in range(1, n+1):
		a = str(i).rjust(l)
		b = oct(i)[2:].rjust(l)
		c = hex(i).upper()[2:].rjust(l)
		d = bin(i)[2:].rjust(l)
		x = a + " " + b + " " + c + " " + d
		arr.append(x)
	print(*arr, sep = "\n")
	return ""


n = int(input())
format(n)
