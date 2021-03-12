string = input()
out = ""
if string[-2:] == "AM" and string[:2] == "12":
	out = "00" + string[2:-2]
elif string[-2:] == "AM":
	out = string[:-2]
elif string[-2:] == "PM" and string[:2] == "12":
	out = "12" + string[2:-2]
else:
	out = str(int(string[:2]) + 12) + string[2:-2]
print(out)
