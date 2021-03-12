s = input()
alnum = False
alpha = False
digit = False
lower = False
upper = False
for x in s:
	if not alnum:
		alnum = x.isalnum()
	if not alpha:
		alpha = x.isalnum() and not x.isdigit()
	if not digit:
		digit = x.isdigit()
	if not lower:
		lower = x.islower()
	if not upper:
		upper = x.isupper()
print(alnum, alpha, digit, lower, upper, sep = "\n")
