for _ in range(int(input())):
	score = {1: 0, 2: 0, 3: 0, 4: 0,
			 5: 0, 6: 0, 7: 0, 8: 0}
	n = int(input())
	sol = []
	for _ in range(n):
		sol.append(list(map(int, input().split())))
	for x in sol:
		if x[0] in score.keys():
			score[x[0]] = max(score[x[0]], x[1])
	print(sum(list(score.values())))
