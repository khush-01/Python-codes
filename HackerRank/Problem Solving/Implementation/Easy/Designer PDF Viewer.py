arr = list(map(int, input().split()))
word = input()
h = 0
for x in word:
	if arr[ord(x)-ord('a')] > h:
		h = arr[ord(x)-ord('a')]
print(h * len(word))
