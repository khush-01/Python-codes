n = int(input())
a = list(map(int, input().split()))
d = n
cnt = {}
for i in range(n):
	try:
		d = min(i-cnt[a[i]], d)
		cnt[a[i]] = i
	except:
		cnt[a[i]] = i
if d == n:
	print(-1)
else:
	print(d)
