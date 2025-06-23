from dataclasses import dataclass

@dataclass(slots=True)
class BaseFile:
    name: str
    type: str
    size: int
    extension: str

    def __post_init__(self):
        if self.extension is None:
            raise ValueError("This is not a valid file (missing extension).")
        
    def __str__(self) -> str:
        return f'{self.name}.{self.extension}'
