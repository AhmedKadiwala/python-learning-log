# Write a python function to print multiplication table of a given number.
def table(n):
    for i in range(1,11):
        print(f"{n}x{i} = {n*i}")
    return 0

x = int(input("Enter number for table printing:"))
table(x)