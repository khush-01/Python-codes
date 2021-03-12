def leap(yr):
	if yr < 1918:
		return yr % 4 == 0
	elif yr > 1918:
		if yr % 100 == 0:
			return yr % 400 == 0
		else:
			return yr % 4 == 0


year = input()
if year == "1918":
	date = "26"
else:
	if leap(int(year)):
		date = "12"
	else:
		date = "13"
print(date + ".09." + year)
