def bins(n):
	cnt = 0
	for x in n:
		if x == '1':
			cnt += 1
	return cnt


for _ in range(int(input())):
	num = int(input())
	if num < 4096:
		print(bins(bin(num)))
	else:
		tot = 0
		while num > 0:
			tot += bins(bin(min(2048, num)))
			num -= 2048
		print(tot)
