for _ in range(int(input())):
	cnt = {}
	n = int(input())
	a = list(map(int, input().split()))
	for x in a:
		if x in cnt.keys():
			cnt[x] += 1
		else:
			cnt[x] = 1
	print(sum(cnt.values()) - max(cnt.values()))
