from typing import List

from helper.types.base_class import BaseFile


class CodeFile(BaseFile):
    _extensions: List[str] = ['js', 'py', 'cpp', 'java', 'bat', 'css', 'html']

    def __init__(self, 
                _name: str, 
                _type: str, 
                _size: int, 
                _extension: str
                ) -> None:
        
        super().__init__(_name, _type, _size, _extension)

        if _extension and _extension not in self._extensions:
            return # either not a file or the proper extension (?)

    def __str__(self):
        return {'name': self._name, 
                'extension': self._extension, 
                'type': self._type, 
                'size': self._size
                }
    

    

    
    
