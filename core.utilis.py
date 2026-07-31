"""
Utility functions for SyncFusion.
"""

from pathlib import Path
import hashlib


def create_folder(folder_path):
    """
    Create a folder if it does not exist.
    """
    Path(folder_path).mkdir(
        parents=True,
        exist_ok=True
    )


def get_relative_path(file_path, base_folder):
    """
    Return the relative path of a file.
    """
    return Path(file_path).relative_to(base_folder)


def calculate_hash(file_path):
    """
    Calculate the SHA-256 hash of a file.
    """
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()
