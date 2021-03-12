s = input()
flag = 1
arr = [False] * 26
for x in s.lower():
	if x == " ":
		continue
	rank = ord(x) - ord('a')
	if arr[rank] == True:
		continue
	elif arr[rank] == False:
		arr[rank] = True
for x in arr:
	if x == False:
		flag = 0
		break
if flag:
	print("pangram")
else:
	print("not pangram")
