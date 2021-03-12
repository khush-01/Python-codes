def mutate(s, pos, char):
	return s[:pos] + char + s[pos+1:]


s = input()
i, c = input().split()
print(mutate(s, int(i), c))
