#10 Try to sort an array if you can then try without sort method

arr = [11,45,34,32,76,87,45]
newarr = []

while arr:
	min = arr[0]
	for i in arr:
		if i<min:
			min = i
	newarr.append(min)
	arr.remove(min)
print(newarr)