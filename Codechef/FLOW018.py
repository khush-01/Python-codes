fact = [1]
for i in range(1, 21):
	fact.append(0)
	fact[i] = fact[i-1] * i

for _ in range(int(input())):
	print(fact[int(input())])
