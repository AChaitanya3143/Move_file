import os
import shutil

from_dir = "C:/Users/HP/Downloads/Document_Files"
to_dir = "C:/Users/HP/Downloads/Document_Files"

if not os.path.exists(to_dir):
    os.makedirs(to_dir)

list_of_files = os.listdir(from_dir)
print(list_of_files) 

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    print(f"Name: {name}, Extension: {extension}") 
