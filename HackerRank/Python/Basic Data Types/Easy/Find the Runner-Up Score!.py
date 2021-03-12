n = int(input())
arr = [int(x) for x in input().split()]
arr = list(dict.fromkeys(arr))
arr.sort()
print(arr[-2])
