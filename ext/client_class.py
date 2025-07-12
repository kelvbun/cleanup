from pathlib import Path
from typing import ClassVar, List, Iterable

from helper.types.folder import FolderFile
from helper.types.files import BaseFile
from helper.types.files import CodeFile
from helper.types.files import ExecutableFile
from helper.types.files import ImageFile


class FileManager:
    files: ClassVar[List[BaseFile]] = []
    type_extensions: ClassVar[dict[str, List[str]]] = {
        'image': ImageFile.extensions, 
        'executable': ExecutableFile.extensions, 
        'code': CodeFile.extensions
    }

    def try_cleanup(self, files: str | Iterable[str]):
        if isinstance(files, str):
            files = [files]

        for file in files:
            file = Path(file)
            file.unlink()
            print(f'removed {file} from directory')
        
    def map_directory(self, dir: str):
        path = Path(dir)

        if path.exists():
            print(path.rglob())