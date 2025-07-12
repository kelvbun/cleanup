from dataclasses import dataclass
from typing import ClassVar, List
from helper.files.base_file import BaseFile

@dataclass(slots=True)
class ImageFile(BaseFile):
    dimension: str
    extensions: ClassVar[List[str]] = ['png', 'webp', 'jpg', 'jpeg', 'svg', 'gif']

    def __post_init__(self):
        super().__post_init__()

    def __str__(self) -> str:
        return f"{super().__str__()} ({self.dimension})"
