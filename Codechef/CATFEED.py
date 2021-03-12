for _ in range(int(input())):
	n, m = map(int, input().split())
	a = list(map(int, input().split()))
	cnt = {x: 0 for x in range(1, n+1)}
	flag = 1
	for x in a:
		if x in cnt.keys():
			cnt[x] += 1
		if max(cnt.values()) - min(cnt.values()) > 1:
			flag = 0
			break
	if flag:
		print("YES")
	else:
		print("NO")
