l, b = int(input()), int(input())
a = l * b
p = 2 * (l + b)
if a > p:
	print("Area", a, sep = "\n")
elif p > a:
	print("Peri", p, sep = "\n")
else:
	print("Eq", a, sep = "\n")
