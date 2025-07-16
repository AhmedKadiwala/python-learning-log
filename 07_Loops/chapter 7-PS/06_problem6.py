# print factorial of number 
i = 1
fact = 1
n = int(input("Enter the number:"))
while(i < n+1):
    fact = fact * i
    i = i + 1

print(fact)