'''
Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*
'''

def reverseTri(n):
    for i in range (0,n):
        print("*"*(n-i))
    return 0

a = int(input("Enter a number:"))
reverseTri(a)