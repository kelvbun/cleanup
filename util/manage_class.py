import os
from typing import List, Union

from util.types.base_class import BaseFile
from util.types.image_class import ImageFile


class FileManager:
    _files: List[BaseFile] = []
    _types: dict = {'image': ImageFile._extensions}

    @property
    def files(self):
        return self._files

    def try_cleanup(self, files: Union[str, List[str]]):
        if isinstance(files, str):
            os.remove(files)
            print(f'removed {file} from directory')

        if isinstance(files, list):
            for file in files:
                os.remove(file)
                print(f'removed {file} from directory')
    
    def try_access(self, dir: str):
        if os.scandir(dir):
            return True
        else:
            return False
        
    def fetch_files(self, dir: str):
        if self.try_access(dir):
            for file in os.listdir(dir):
                extension = file.split('.')

                if not len(extension) < 2:
                    for key, value in self._types.items():
                        if extension[-1] in value:
                            self._files.append(ImageFile(file, key, 1, extension, '2x2')._name)

            return self._files
        
    
        