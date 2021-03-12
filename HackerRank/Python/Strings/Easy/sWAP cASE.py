s = input()
out = ""
for x in s:
	if ord('a') <= ord(x) <= ord('z'):
		out += chr(ord(x) - ord('a') + ord('A'))
	elif ord('A') <= ord(x) <= ord('Z'):
		out += chr(ord(x) - ord('A') + ord('a'))
	else:
		out += x
print(out)
