from dataclasses import dataclass

from typing import ClassVar, List

@dataclass()
class BaseFile:
    name: str
    type: str
    size: int
    extension: str

    extensions: ClassVar[List[str]] = ['txt', 'docx', 'pdf', 'md', 'gitignore']

    def __post_init__(self):
        if not self.extension:
            raise ValueError("This is not a valid file (missing extension).")
        
        if self.extension and self.extension.lower() not in self.extensions:
            raise ValueError(
                f"Invalid file extension '{self.extension}' for {str(self)}.\n"
                f"To allow this extension, consider updating the 'extensions' class variable accordingly."
            )

    def __str__(self) -> str:
        return f'{self.name}'
