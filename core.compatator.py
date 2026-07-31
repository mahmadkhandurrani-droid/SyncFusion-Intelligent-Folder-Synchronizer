"""
Compare source and destination folders.
"""

from core.utils import calculate_hash


class FolderComparator:
    """
    Compare files between two folders.
    """

    def compare(
        self,
        source_files,
        destination_files,
        source_root,
        destination_root
    ):

        source_map = {
            file.relative_to(source_root): file
            for file in source_files
        }

        destination_map = {
            file.relative_to(destination_root): file
            for file in destination_files
        }

        new_files = []
        modified_files = []
        deleted_files = []

        for relative_path, source_file in source_map.items():

            destination_file = destination_map.get(relative_path)

            if destination_file is None:
                new_files.append(source_file)

            elif calculate_hash(source_file) != calculate_hash(destination_file):
                modified_files.append(source_file)

        for relative_path, destination_file in destination_map.items():

            if relative_path not in source_map:
                deleted_files.append(destination_file)

        return (
            new_files,
            modified_files,
            deleted_files
        )
