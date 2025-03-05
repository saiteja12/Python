import os

# Specify the folder path
folder_path = "path/to/your/folder"

# Get a list of files in the folder
files = os.listdir(folder_path)

# Loop through the files and print only file names (ignore directories)
for file in files:
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):  # Check if it's a file, not a directory
        print(file)
