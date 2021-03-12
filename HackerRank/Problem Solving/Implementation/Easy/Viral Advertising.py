n = int(input())
people = 5
liked = 2
total = 2
for x in range(2, n+1):
	people = 3 * liked
	liked = people // 2
	total += liked
print(total)
