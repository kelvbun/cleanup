from helper.client_class import FileManager
from helper.files.base_file import BaseFile


#manager = FileManager()
#print(manager.fetch_files('/Users/kelvin/Documents/code/cleanup'))
#manager.try_cleanup(manager._files)

base = BaseFile(
    'a file',
    'image',
    20,
    'png'
)

print(str(base))