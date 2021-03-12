n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
	op, m = map(str, input().split())
	a = set(map(int, input().split()))
	if op == "update":
		s |= a
	elif op == "intersection_update":
		s &= a
	elif op == "difference_update":
		s -= a
	else:
		s ^= a
print(sum(s))
