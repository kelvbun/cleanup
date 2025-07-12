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
    

@dataclass()
class CodeFile(BaseFile):
    extensions: ClassVar[List[str]] = ['js', 'py', 'cpp', 'java', 'css', 'html']
    
    def __post_init__(self):
        super().__post_init__()


@dataclass
class ExecutableFile(BaseFile):
    extensions: ClassVar[List[str]] = ['exe']

    def __post_init__(self):
        super().__post_init__()


@dataclass(slots=True)
class ImageFile(BaseFile):
    dimension: str
    extensions: ClassVar[List[str]] = ['png', 'webp', 'jpg', 'jpeg', 'svg', 'gif']

    def __post_init__(self):
        super().__post_init__()

    def __str__(self) -> str:
        return f"{super().__str__()} ({self.dimension})"
    
