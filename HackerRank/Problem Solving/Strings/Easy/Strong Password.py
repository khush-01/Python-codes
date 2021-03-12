l = int(input())
s = input()
small = 0
large = 0
num = 0
spchar = 0
for x in s:
	if ord('a') <= ord(x) <= ord('z'):
		small = 1
	elif ord('A') <= ord(x) <= ord('Z'):
		large = 1
	elif ord('0') <= ord(x) <= ord('9'):
		num = 1
	else:
		spchar = 1
total = small + large + num + spchar
print(max(4 - total, 6 - l))
