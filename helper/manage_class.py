import os
from typing import List, Union

from helper.types.base_class import BaseFile
from helper.types.image_class import ImageFile
from helper.types.document_class import DocumentFile
from helper.types.executable_class import ExecutableFile
from helper.types.code_class import CodeFile


class FileManager:
    _files: List[BaseFile] = []
    _type_extensions: dict = {'image': ImageFile._extensions, 'document': DocumentFile._extensions, 'executable': ExecutableFile._extensions, 'code': CodeFile._extensions}

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
                    for key, value in self._type_extensions.items():
                        if extension[-1] in value:
                                    
                            if key == 'image':
                                self._files.append(ImageFile(file, key, 1, extension, '2x2')._name)
                                    
                            if key == 'executable':
                                self._files.append(ExecutableFile(file, key, 1, extension)._name)

                            if key == 'document':
                                self._files.append(DocumentFile(file, key, 1, extension)._name)

                            if key == 'code':
                                self._files.append(CodeFile(file, key, 1, extension)._name)

            return self._files
        
    
        