def brac(s):
	mxm = 0
	bal = 0
	for x in s:
		if x == '(':
			bal += 1
		else:
			bal -= 1
		mxm = max(mxm, bal)
	return mxm


for _ in range(int(input())):
	a = input()
	res = brac(a)
	print('(' * res + ')' * res)
