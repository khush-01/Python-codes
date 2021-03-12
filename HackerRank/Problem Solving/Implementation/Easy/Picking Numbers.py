n = int(input())
a = list(map(int, input().split()))
dic = {}
for x in a:
	if x in dic.keys():
		dic[x] += 1
	else:
		dic[x] = 1
seq = 0
for x in dic.keys():
	seq = max(seq, dic[x])
	if x + 1 in dic.keys():
		seq = max(seq, dic[x] + dic[x+1])
print(seq)
