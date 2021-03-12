n = int(input())
arr = []
for _ in range(n):
	arr.append(list(map(str, input().split())))
lis = []
for x in arr:
	if x[0] == "insert":
		lis.insert(int(x[1]), int(x[2]))
	elif x[0] == "remove":
		lis.remove(int(x[1]))
	elif x[0] == "append":
		lis.append(int(x[1]))
	elif x[0] == "sort":
		lis.sort()
	elif x[0] == "pop":
		lis.pop()
	elif x[0] == "reverse":
		lis = lis[::-1]
	else:
		print(lis)
