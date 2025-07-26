import os

# Step 1: Create a folder for the tables
folder_name = "C:\\Users\\Ahmed Kadiwala\\Desktop\\python-oneshot\\09_File_IO\\chapter 9 -PS\\Tables_for_13yo"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"✅ Folder '{folder_name}' created.")
else:
    print(f"📁 Folder '{folder_name}' already exists.")

# Step 2: Generate tables from 2 to 20
for num in range(2, 21):
    filename = f"Table_of_{num}.txt"
    filepath = os.path.join(folder_name, filename)

    with open(filepath, "w") as f:
        f.write(f"Multiplication Table of {num}\n")
        f.write("-" * 30 + "\n")

        for i in range(1, 11):
            line = f"{num} x {i} = {num * i}"
            f.write(line + "\n")

    print(f"✅ {filename} created.")
