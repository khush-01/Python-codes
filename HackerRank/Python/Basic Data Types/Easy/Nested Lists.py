n = int(input())
arr = []
marks = []
for _ in range(n):
	name = input()
	marks.append(float(input()))
	arr.append([name, marks[-1]])
arr.sort(key = lambda x:x[0])
marks.sort()
low = min(marks)
while marks[0] == low:
	marks.pop(0)
lis = list(x[0] for x in arr if x[1] == min(marks))
print(*lis, sep = "\n")
