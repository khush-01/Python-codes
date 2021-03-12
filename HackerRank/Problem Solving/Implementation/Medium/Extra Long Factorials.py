def factorial(num):
	fact = [1]
	for i in range(1, num+1):
		fact.append(0)
	for i in range(1, num+1):
		fact[i] = fact[i-1] * i
	return fact[num]


print(factorial(int(input())))
