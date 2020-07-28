#3 Write a Python program which accepts the user's first and last name and 
#print them in reverse order with a space between them.


f_name = str(input("Enter your First Name: "))
l_name = str(input("Enter your Last Name: "))
print("Full name in reverse order is: ",f_name[::-1], l_name[::-1])