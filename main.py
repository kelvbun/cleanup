from helper.client_class import FileManager

manager = FileManager()
print(manager.fetch_files('/Users/kelvin/Documents/code/cleanup'))
#manager.try_cleanup(manager._files)

