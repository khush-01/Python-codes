x, y = map(float, input().split())
print("{:.2f}".format(y-x-0.5) if y - x - 0.5 > 0 and x % 5 == 0 else "{:.2f}".format(y))
