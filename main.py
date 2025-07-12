from helper.client_class import FileManager
from helper.types.files import BaseFile

from pathlib import Path

#manager = FileManager()
#print(manager.map_directory(r'C:\Users\ii_sk\OneDrive\Code\cleanup'))

path = Path(r'C:\Users\ii_sk\OneDrive\Code\cleanup')

for item in path.rglob("*"):
    if item.is_file():
        print("File:", item)
    elif item.is_dir():
        print("Folder:", item)