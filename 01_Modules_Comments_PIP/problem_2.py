import os

# Specify the directory path
directory_path = '/'  # '.' refers to the current directory

# List all entries in the specified directory
entries = os.listdir(directory_path)

print(f"Contents of '{directory_path}':")
for entry in entries:
    print(entry)
