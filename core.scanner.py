"""
Folder scanning module.
"""

from pathlib import Path


class FolderScanner:
    """
    Scan folders recursively.
    """

    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)

    def scan(self):
        """
        Return all files inside the folder.
        """
        if not self.folder_path.exists():
            raise FileNotFoundError(
                f"Folder not found: {self.folder_path}"
            )

        return [
            file
            for file in self.folder_path.rglob("*")
            if file.is_file()
        ]
