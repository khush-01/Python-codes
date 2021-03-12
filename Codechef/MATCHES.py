count = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4,
		 '5': 5, '6': 6, '7': 3, '8': 7, '9': 6}

for _ in range(int(input())):
	a, b = map(int ,input().split())
	tot = 0
	s = str(a + b)
	for x in s:
		tot += count[x]
	print(tot)
