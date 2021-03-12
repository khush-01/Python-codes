n = int(input())
arr = {}
for _ in range(n):
	name, *marks = input().split()
	marks = [float(x) for x in marks]
	arr[name] = marks
q = input()
print("{:.2f}".format((arr[q][0] + arr[q][1] + arr[q][2]) / 3))
