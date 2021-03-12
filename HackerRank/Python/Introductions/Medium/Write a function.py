def is_leap(yr):
	if yr % 100 == 0:
		return yr % 400 == 0
	else:
		return yr % 4 == 0

print(is_leap(int(input())))
