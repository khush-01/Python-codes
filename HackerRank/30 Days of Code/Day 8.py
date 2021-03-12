a = {}
n = int(input())
for _ in range(n):
	x, y = map(str, input().split())
	a[x] = y
try:
	while True:
		x = input()
		if x in a.keys():
			print(x + "=" + a[x])
		else:
			print("Not found")
except EOFError:
	pass
