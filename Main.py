from DirectoryTraversal import *

def compare_two_paths_file_count():
    path1: str = input("Give a path: ")
    path2: str = input("Give another path: ")

    d1: object = DirectoryTraversal(path1)
    d2: object = DirectoryTraversal(path2)

    count1: int = d1.count_files()
    count2: int = d2.count_files()

    print("path " + str(path1) + " has " + str(count1) + " files and path " + str(path2) + " has " + str(
        count2) + " files")


# Main

compare_two_paths_file_count()

# CR: the next next will be to print the files instead of counting them. After that I want you to try to think how to implement it without recursion (a little hard).
