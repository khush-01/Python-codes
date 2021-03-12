string = input()
substr = input()
subs = [string[i:i+len(substr)] for i in range(len(string)-len(substr)+1)]
count = 0
for x in subs:
	if x == substr:
		count += 1
print(count)
