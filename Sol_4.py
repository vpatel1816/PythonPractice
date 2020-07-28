#4 Write a Python program to accept a filename from the 
#user and print the extension of that. 

file_name = str(input("Enter the File Name: "))
extension = file_name.split(".")
print("Extension is : ",extension[1])