from textwrap import wrap


s = input()
n = int(input())
print(*wrap(s, n), sep = "\n")
