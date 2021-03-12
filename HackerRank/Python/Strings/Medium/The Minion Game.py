s = input()
l = len(s)
ksc = 0
ssc = 0
for x in range(l):
	if s[x] in "AEIOU":
		ksc += l - x
	else:
		ssc += l - x
if ksc > ssc:
	print("Kevin", ksc)
elif ssc > ksc:
	print("Stuart", ssc)
else:
	print("Draw")
