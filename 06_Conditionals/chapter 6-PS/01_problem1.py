# Write a program to find the greatest of four numbers entered by the user.

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
d = int(input("Enter 4th number: "))

if (a>b and a>c and a>d):
    print("Greatest number is a: ",a)

elif (b>c and b>d):
    print("Greatest number is b: ",b)

elif(c>d):
    print("Greatest number is c: ",c)

else:
    print("Greatest number is d: ",d)  
