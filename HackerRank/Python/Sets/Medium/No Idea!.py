n, m = map(int, input().split())
l = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
cnt = 0
for x in l:
	if x in a:
		cnt += 1
	if x in b:
		cnt -= 1
print(cnt)
