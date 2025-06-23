from typing import ClassVar, List
from helper.files.base_file import BaseFile

class CodeFile(BaseFile):
    extensions: ClassVar[List[str]] = ['js', 'py', 'cpp', 'java', 'css', 'html']

    def __post_init__(self):
        if self.extension and self.extension not in self.extensions:
            raise ValueError(f"Invalid code file extension: {self.extension}")
