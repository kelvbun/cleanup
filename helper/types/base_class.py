class BaseFile:
    def __init__(self, _name: str, _type: str, _size: int, _extension: str) -> None:
        self._name: str = _name
        self._type: str = _type
        self._size: int = _size
        self._extension: str = _extension

        if not _extension: 
            return # this is not a file (?)

    def __str__(self):
        return {'name': self._name, 'extension': self._extension, 'type': self._type, 'size': self._size}
    
    