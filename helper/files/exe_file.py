from dataclasses import dataclass

from typing import ClassVar, List
from helper.files.base_file import BaseFile


@dataclass
class ExecutableFile(BaseFile):
    extensions: ClassVar[List[str]] = ['exe']

    def __post_init__(self):
        super().__post_init__()
    



    

    

    
    
