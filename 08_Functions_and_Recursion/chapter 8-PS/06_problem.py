def inchesTocms(m):
    m = 2.54*m
    return m

a = int(input("Enter a number: "))
print(f"Inches to centimeters = {inchesTocms(a)}")