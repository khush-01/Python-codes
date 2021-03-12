s = input()
lis = [s[i:i+3] for i in range(0, len(s), 3)]
count = 0
for x in lis:
	if x != "SOS":
		for i in range(3):
			if (i == 0 or i == 2) and x[i] != "S":
				count += 1
			elif i == 1 and x[i] != "O":
				count += 1
print(count)
