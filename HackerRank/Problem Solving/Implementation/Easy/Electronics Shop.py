b, n, m = map(int, input().split())
key = list(map(int, input().split()))
usb = list(map(int, input().split()))
key.sort()
usb.sort()
cost = -1
for x in key:
	for y in usb:
		pay = x+y
		if pay <= b:
			cost = max(cost, pay)
print(cost)
