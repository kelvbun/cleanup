from typing import List

from util.types.base_class import BaseFile


class ImageFile(BaseFile):
    _extensions: List[str] = ['png', 'webp', 'jpg', 'jpeg', 'svg', 'gif']

    def __init__(self, _name, _type, _size, _extension, _dimension):
        super().__init__(_name, _type, _size, _extension)
        self._dimension = _dimension

        if _extension and _extension not in self._extensions:
            return # either not a file or the proper extension (?)

    def __str__(self):
        return f'name: {self._name}, type: {self._type}, size: {self._size}, dimension: {self._dimension}'

    @property
    def dimension(self):
        return self._dimension
    
    @dimension.setter
    def dimension(self, value):
        return print('we cant resize this!')
    

    

    
    
