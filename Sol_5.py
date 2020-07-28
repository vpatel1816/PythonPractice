#5 Write a Python program to display the 
#first and last colors from the following list. Go to the editor



colorList = input("Enter the color list with Spaces").split(" ")
print("First Color is: ", colorList[0], "\nLast color is: " ,colorList[len(colorList)-1])