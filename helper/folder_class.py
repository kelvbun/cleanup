from typing import List


class FolderFile:
    def __init__(self, 
                _name: str, 
                _amount: int, 
                _type: str, 
                _size: int, 
                _files: List[dict]
                ) -> None:
        
        self._name: str = _name 
        self._amount: int = _amount
        self._type: str = _type
        self._size: int = _size
        self._files: dict = _files

    @property
    def name(self):
        return self._name
    
    @property
    def amount(self):
        return self._amount
    
    @property
    def type(self):
        return self._type
    
    @property
    def size(self):
        return self._size
    
    @property
    def files(self):
        return self._files

    def __str__(self):
        return {'name': self._name, 
                'amount': self._amount, 
                'type': self._type,
                'size': self._size, 
                'files': self._files
                }




        