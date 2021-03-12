n, m = map(int, input().split())
avg = 0
for _ in range(m):
	a, b, k = map(int, input().split())
	avg += k * (b - a + 1)
print(avg // n)
