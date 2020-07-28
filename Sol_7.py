#7 Find second min and second largest value of a list and their indexes also

int_list = [6,7,8,4,45,56,89,90,98,1999]

min = int_list[0]
second_min = int_list[0]
second_high = int_list[0]

for i in int_list:
	if i < min:
		second_min = min 
		min = i
	else:
		second_high = max
		max = i

print("Min: ",min,",Second Min :", second_min,",Max: ", max,",Second Max: " ,second_high)