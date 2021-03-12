for _ in range(int(input())):
	sal = int(input())
	hra = 500 if sal >= 1500 else 0.1 * sal
	da = 0.98 * sal if sal >= 1500 else 0.9 * sal
	print("{:.3f}".format(sal + hra + da))
