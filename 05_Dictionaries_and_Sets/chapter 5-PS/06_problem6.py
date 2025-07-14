name1 = input("Enter first name: ")
lang1 = input(f"Enter favorite language of {name1}: ")

name2 = input("Enter second name: ")
lang2 = input(f"Enter favorite language of {name2}: ")

name3 = input("Enter third name: ")
lang3 = input(f"Enter favorite language of {name3}: ")

name4 = input("Enter fourth name: ")
lang4 = input(f"Enter favorite language of {name4}: ")


name_language_dict = {
    name1: lang1,
    name2: lang2,
    name3: lang3,
    name4: lang4
}

# Print the dictionary
print("\nName-Language Dictionary:")
print(name_language_dict)
