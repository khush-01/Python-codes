s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
cnt1 = 0
cnt2 = 0
for x in arr1:
	if s <= (x + a) <= t:
		cnt1 += 1
for y in arr2:
	if s <= (y + b) <= t:
		cnt2 += 1
print(cnt1, cnt2, sep="\n")
