players = int(input())
ranks = list(map(int, input().split()))
games = int(input())
score = list(map(int, input().split()))
ranks = list(dict.fromkeys(ranks))
for x in score:
	ranks.append(x)
	ranks = list(dict.fromkeys(ranks))
	ranks.sort(reverse = True)
	print(ranks.index(x) + 1)
