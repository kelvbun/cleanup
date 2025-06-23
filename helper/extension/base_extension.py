from dataclasses import dataclass

@dataclass()
class BaseExtension:
    name: str
    mime_type: str
    category: str
    is_executable: bool = False
