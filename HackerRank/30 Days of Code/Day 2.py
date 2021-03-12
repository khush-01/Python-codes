cost = float(input())
tip = int(input())
tax = int(input())
print(round(cost * (100 + tip + tax) / 100))
