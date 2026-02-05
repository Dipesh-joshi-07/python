import os

# specify the directory path you want to list
directory_path = "/new folder"

try:
    # list contents of the given directory
    contents = os.listdir(directory_path)
    
    # print each item one by one
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("Error: The specified directory does not exist.")
except PermissionError:
    print("Error: You do not have permission to access this directory.")
