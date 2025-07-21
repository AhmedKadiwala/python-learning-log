# Write a python program using function to convert Celsius to Fahrenheit.
def celTOfar(t):
    t = (t*1.8) + 32
    print(t)

x = int(input("Enter temperature in degree celsius:"))
celTOfar(x)