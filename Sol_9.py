#9 wright a program to convert an string into list of characters

line = str(input("Enter the line :"))
chr_list = []
for i in line:
	if i != " ":
		chr_list.append(i)
	else:
		pass
print(chr_list)

