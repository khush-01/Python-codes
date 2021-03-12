fact = [1 for _ in range(101)]
for i in range(2, 101):
	fact[i] = fact[i-1] * i

for _ in range(int(input())):
	print(fact[int(input())])
