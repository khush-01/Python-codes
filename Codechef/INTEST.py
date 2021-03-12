n, k = map(int, input().split())
cnt = 0
for _ in range(n):
	if int(input()) % k == 0:
		cnt += 1
print(cnt)
