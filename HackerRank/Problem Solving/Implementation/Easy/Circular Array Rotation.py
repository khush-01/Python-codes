n, k, q = map(int, input().split())
arr = list(map(int, input().split()))
queries = []
for i in range(q):
	queries.append(int(input()))
dic = {((i + k) % n): arr[i] for i in range(0, n)}
for x in queries:
	print(dic[x])
