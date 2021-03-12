s = input()
count = 1
for x in s:
	if ord('A') <= ord(x) <= ord('Z'):
		count += 1
print(count)
