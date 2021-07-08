from DirectoryTraversal import *


class Main:
    @staticmethod
    def compare_two_paths_file_count():
        path1: str = input("Give a path: ")
        d1 = DirectoryTraversal(path1)
        d1.print_files_using_queue()

        path2: str = input("Give another path: ")
        d2 = DirectoryTraversal(path2)
        d2.print_files_using_queue()

        # count1: int = d1.count_files()
        # count2: int = d2.count_files()
        #
        # print(f"path {path1} has {count1} files and path {path2} has {count2} files")


# Main

Main.compare_two_paths_file_count()
