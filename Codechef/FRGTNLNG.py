for _ in range(int(input())):
	n, k = map(int, input().split())
	words = list(map(str, input().split()))
	phrases = set(map(str, input().split()))
	for _ in range(k-1):
		phrases.update(set(map(str, input().split())))
	out = ""
	for x in words:
		if x in phrases:
			out += 'YES '
		else:
			out += 'NO '
	print(out)
