for _ in range(int(input())):
	s = input()
	slist = [ord(x) for x in s]
	diff = []
	for x in range(len(slist)-1):
		diff.append(abs(slist[x] - slist[x+1]))
	if diff == diff[::-1]:
		print("Funny")
	else:
		print("Not Funny")
