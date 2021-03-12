from math import ceil


n, m = map(int, input().split())
count = ceil(n / 2) * ceil(m /2)
print(count)
