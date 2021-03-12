length = int(input())
string = input()
key = int(input())
msg = ""
for x in string:
	if ord('a') <= ord(x) <= ord('z'):
		msg += chr(((ord(x) - ord('a') + key) % 26) + ord('a'))
	elif ord('A') <= ord(x) <= ord('Z'):
		msg += chr(((ord(x) - ord('A') + key) % 26) + ord('A'))
	else:
		msg += x
print(msg)
