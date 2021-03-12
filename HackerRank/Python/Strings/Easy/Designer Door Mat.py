n, m = map(int, input().split())
pattern = '.|.'
word = "WELCOME"

for x in range(1, n//2+1):
	print((pattern * (2 * x - 1)).center(m, '-'))
print(word.center(m, '-'))
for x in range(n//2, 0, -1):
	print((pattern * (2 * x -1)).center(m, '-'))
