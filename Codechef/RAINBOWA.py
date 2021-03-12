for _ in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))
	if n % 2:
		for x in range(n):
			if x == n//2 + 1:
				if l[x] != 7:
					print("no")
					break
			elif l[x] != l[-1-x]:
				print("no")
				break
		else:
			print("yes")
	else:
		print("no")
