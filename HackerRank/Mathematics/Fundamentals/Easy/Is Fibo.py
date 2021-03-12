fib = [0, 1]
for i in range(2, 100):
	fib.append(fib[i-1] + fib[i-2])

for _ in range(int(input())):
	if int(input()) in fib:
		print("IsFibo")
	else:
		print("IsNotFibo")
