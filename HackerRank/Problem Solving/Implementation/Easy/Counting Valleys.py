level = 0
prev = 0
n = int(input())
path = input()
count = 0
for x in path:
	prev = level
	if x == "D":
		level -= 1
	else:
		level += 1
	if level == 0 and prev < level:
		count += 1
print(count)
