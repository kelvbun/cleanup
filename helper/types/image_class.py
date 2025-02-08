from typing import List

from helper.types.base_class import BaseFile


class ImageFile(BaseFile):
    _extensions: List[str] = ['png', 'webp', 'jpg', 'jpeg', 'svg', 'gif']

    def __init__(self, 
                _name: str, 
                _type: str, 
                _size: int, 
                _extension: str, 
                _dimension: str
                ) -> None:
        
        super().__init__(_name, _type, _size, _extension)
        self._dimension: str = _dimension

        if _extension and _extension not in self._extensions:
            return # either not a file or the proper extension (?)
        
    @property
    def dimension(self):
        return self._dimension

    def __str__(self):
        return {'name': self._name, 
                'extension': self._extension, 
                'type': self._type, 
                'size': self._size
                }
    
    

    

    
    
