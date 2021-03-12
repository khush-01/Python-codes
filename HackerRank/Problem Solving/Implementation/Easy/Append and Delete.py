str1 = input()
str2 = input()
moves = int(input())
count = 0
if str1 == str2:
	print("Yes")
else:
	while len(min(str1, str2)):
		if str1[0] == str2[0]:
			count += 1
			str1 = str1[1:]
			str2 = str2[1:]
		else:
			break
	steps = len(str1 + str2)
	if steps == moves:
		print("Yes")
	elif steps > moves:
		print("No")
	else:
		moves -= steps
		if moves >= (2*count) or moves % 2 == 0:
			print("Yes")
		else:
			print("No")
