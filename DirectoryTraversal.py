import os.path


class DirectoryTraversal:
    path: str = ""

    def __init__(self, path: str) -> None:
        self.path = path


    def count_files(self) -> int:
        file_count: int = 0
        files = os.listdir(self.path)
        for i in range(len(files)):
            path_in_path: str = os.path.join(self.path, files[i])
            if os.path.isdir(path_in_path):
                file_count += DirectoryTraversal(path_in_path).count_files()
            else:
                file_count += 1

        return file_count
