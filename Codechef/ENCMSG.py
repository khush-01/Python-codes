def encode(s):
	res = ""
	for x in s:
		char = chr(ord('z') + ord('a') - ord(x))
		res += char
	return res


def xchange(s):
	s = list(s)
	l = len(s)
	for i in range(0, l, 2):
		if i + 1 < l:
			s[i], s[i+1] = s[i+1], s[i]
	s = ''.join(s)
	return s


for _ in range(int(input())):
	n = int(input())
	print(encode(xchange(input())))
