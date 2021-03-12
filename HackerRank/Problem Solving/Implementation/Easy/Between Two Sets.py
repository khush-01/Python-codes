def ismultipleof(arr, num):
	for i in arr:
		if num % i != 0:
			return False
	return True


def isfactorof(arr, num):
	for i in arr:
		if i % num != 0:
			return False
	return True


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
count = 0
for x in range(a[-1], b[0]+1):
	if ismultipleof(a, x) and isfactorof(b, x):
		count += 1
print(count)
