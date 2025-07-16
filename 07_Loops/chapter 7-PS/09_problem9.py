'''
Write a program to print the following star pattern.
* * *
*   *     for n = 3
* * *
'''

n = int(input("Enter the size (n): "))

for i in range(n):
    for j in range(n):
        # Print stars at the borders
        if i == 0 or i == n-1  or j == 0 or j == n-1 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # Move to the next line
