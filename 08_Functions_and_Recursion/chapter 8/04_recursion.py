def factorial(n):
    if n == 0 or n == 1: # base condition which doesn’t call the function any further
        return 1
    else:
        return n*factorial(n-1) # function calling itself
    
a = int(input("Enter a number:"))
print(f"Factorial:{factorial(a)}")
    
