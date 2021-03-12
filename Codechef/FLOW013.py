for _ in range(int(input())):
	if sum([int(x) for x in input().split()]) == 180:
		print("YES")
	else:
		print("NO")
