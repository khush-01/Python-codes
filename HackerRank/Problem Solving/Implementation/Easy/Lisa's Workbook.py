n, k = map(int, input().split())
l = list(map(int, input().split()))
cnt = 0
i = 0
j = 1
m = 1
while i < n:
    if m <= j and j <= min(m + k - 1, l[i]):
        cnt += 1
    j += 1
    m += k
    if m > l[i]:
        i += 1
        m = 1
print(cnt)
