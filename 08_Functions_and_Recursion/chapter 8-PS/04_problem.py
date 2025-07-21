# Write a recursive function to calculate the sum of first n natural numbers
def sumOfn(n):
    sum = 0
    for i in range (0,n):
        i  = i + 1
        sum = sum + i
    return sum

n = int(input("Enter a number:"))
print(f"The sum of from 1 to given number: {sumOfn(n)}")