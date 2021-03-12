def place(x, y):
	return y - m * x - c


n = int(input())
m, c = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]
pow1 = 0
pow2 = 0
for x in p:
	if place(x[0], x[1]) < 0:
		pow1 += x[2]
	else:
		pow2 += x[2]
print(max(pow1, pow2))
