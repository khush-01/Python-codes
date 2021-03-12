def priority(op):
	p = {'+': 0, '-': 1, '*': 2, '/': 3, '^': 4, '(': 5}
	return p[op]


for _ in range(int(input())):
	stk = []
	out = ""
	s = input()
	for x in s:
		if ord('a') <= ord(x) <= ord('z'):
			out += x
		elif x == '(':
			stk.append(x)
		elif x == ')':
			while stk[-1] != '(':
				out += stk.pop()
			stk.pop()
		else:
			while priority(x) >= priority(stk[-1]):
				out += stk.pop()
			stk.append(x)
	print(out)
