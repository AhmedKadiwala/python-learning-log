import re

# Step 1: Read the original content from the file
with open("C:\\Users\\Ahmed Kadiwala\\Desktop\\python-oneshot\\09_File_IO\\chapter 9 -PS\\example.txt", "r") as file:
    content = file.read()

# Step 2: Use regex to replace all case-insensitive occurrences of "donkey"
updated_content = re.sub(r"donkey", "#####", content, flags=re.IGNORECASE)

# Step 3: Write the updated content back to the same file
with open("example.txt", "w") as file:
    file.write(updated_content)

print("✅ All variations of 'Donkey' replaced with '#####'.")