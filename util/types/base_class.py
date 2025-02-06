class BaseFile:
    def __init__(self, _name, _type, _size, _extension):
        self._name = _name
        self._type = _type
        self._size = _size
        self._extension = _name.split('.')[1]

        if not _extension: 
            return # this is not a file (?)

    def __str__(self):
        return f'name: {self._name}.{self._extension}, type: {self._type}, size: {self._size}'
    
    