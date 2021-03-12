from random import choice

x = choice([1, 2, 3])
print(x, flush = True)
y = int(input())
print(y ^ x, flush = True)
