def arrsum(arr):
	sum = 0
	for x in arr:
		sum += x
	return sum


n, k = map(int, input().split())
bill = list(map(int, input().split()))
amt = int(input())
bill.pop(k)
pay = arrsum(bill) // 2
if amt == pay:
	print("Bon Appetit")
else:
	print(amt - pay)
