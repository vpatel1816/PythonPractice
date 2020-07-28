#8 wright a program to split a list into two sub list from the middle

newlist = [1,2,3,4,5,6,7]
firstlist = []
secondlist = []

mid = int(len(newlist)/2)

for i in range(int(len(newlist)/2)):
	firstlist.append(newlist[i])

for i in range(mid):
	secondlist.append(newlist[i+mid])

print(firstlist, secondlist, mid)