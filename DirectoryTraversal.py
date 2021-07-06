import os.path


class DirectoryTraversal:
    path: str = ""


    def __init__(self, path: str) -> None:
        self.path = path

    def count_files(self) -> int:
        files: list = os.listdir(self.path)
        file_count: int = 0
        for file in files:
            file_path: str = os.path.join(self.path, file)

            if os.path.isdir(file_path):
                file_count += DirectoryTraversal(file_path).count_files()
            else:
                file_count += 1
                print(self.path + "\\" + file + " , size: " + str(os.path.getsize(file_path)))
        return file_count



