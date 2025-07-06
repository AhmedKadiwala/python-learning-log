import os

directory_path = '.'
entries = os.listdir(directory_path)

print(f"Contents of '{directory_path}':")
for entry in entries:
    print(entry)
