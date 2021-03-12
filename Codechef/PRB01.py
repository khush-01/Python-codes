prime = [True for _ in range(100001)]
prime[0] = prime[1] = False
p = 2
while p <= 1000:
	if prime[p] == True:
		for i in range(p*p, 100001, p):
			prime[i] = False
	p += 1

for _ in range(int(input())):
	if prime[int(input())]:
		print("yes")
	else:
		print("no")
