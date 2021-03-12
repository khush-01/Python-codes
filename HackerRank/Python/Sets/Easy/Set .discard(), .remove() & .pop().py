n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
	line = list(input().split())
	if line[0] == "pop":
		s.pop()
	elif line[0] == "discard":
		s.discard(int(line[1]))
	else:
		s.remove(int(line[1]))
print(sum(s))
