from typing import List

from helper.types.base_class import BaseFile


class DocumentFile(BaseFile):
    _extensions: List[str] = ['docx', 'pdf']

    def __init__(self, _name, _type, _size, _extension):
        super().__init__(_name, _type, _size, _extension)

        if _extension and _extension not in self._extensions:
            return # either not a file or the proper extension (?)

    def __str__(self):
        return f'name: {self._name}, type: {self._type}, size: {self._size}'

    

    
    
