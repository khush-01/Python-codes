string = input()
n = int(input())
num = n // len(string)
count = 0
for x in string:
	if x == 'a':
		count += 1
count *= num
for x in string[:n % len(string)]:
	if x == 'a':
		count += 1
print(count)
