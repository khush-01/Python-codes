def roundup(num):
	if num < 38:
		return num
	else:
		rem = num % 5
		if rem >= 3:
			return num + 5 - rem
		else:
			return num

for _ in range(int(input())):
	print(roundup(int(input())))
