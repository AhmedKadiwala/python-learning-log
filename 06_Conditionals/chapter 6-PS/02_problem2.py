'''
Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass.
Assume 3 subjects and take marks as an input from the user.
'''

mat = int(input("Enter maths marks: "))
eng = int(input("Enter english marks: "))
sci = int(input("Enter science marks: "))

total = int((mat+sci+eng)/3)

if (mat >= 33 and sci >= 33 and eng >= 33 and total >= 40 ):
    print("Student has passed successfully.")
else:
    print("Student has failed.")
    





