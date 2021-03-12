n = int(input())
a = list(map(int, input().split()))
cl = 0
cu = 0
for x in a:
	if x % 2:
		cu += 1
	else:
		cl += 1
if cl > cu:
	print("READY FOR BATTLE")
else:
	print("NOT READY")
