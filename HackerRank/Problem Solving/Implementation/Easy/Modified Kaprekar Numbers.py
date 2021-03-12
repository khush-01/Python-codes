def kaprekar(n):
	str1 = str(n)
	d = len(str1)
	num = n * n
	str2 = str(num)
	while len(str2) != 2*d:
		str2 = "0" + str2 
	left, right = "", ""
	for x in range(d):
		left += str2[x]
	for x in range(d, 2*d):
		right += str2[x] 
	total = int(left) + int(right)
	if total == n:
		return True
	else:
		return False


p = int(input())
q = int(input())
out = []
for x in range(p, q+1):
	if kaprekar(x):
		out.append(x)
if len(out) == 0:
	print("INVALID RANGE")
else:
	print(*out)
