# Write a program using functions to find greatest of three numbers
def greatestNum(a,b,c):
    if(a>b and a>c):
        print(f"Greatest of the three: {a}")
    elif(b>c):
        print(f"Greatest of the three: {b}")
    else:
        print(f"Greatest of the three: {c}")

x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
z = int(input("Enter third number:"))

greatestNum(x,y,z)