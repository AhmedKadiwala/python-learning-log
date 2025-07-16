name_list = ["Ahmed", "Shakeel", "John", "Michael"]

name = input("Enter a name: ")

if name in name_list:
    print(f"{name} is present in the list.")
else:
    print(f"{name} is not present in the list.")