# input: two directory paths
# output: print which directory has more files (recursively)
# notes: you can use os.listdir and os.path.isdir but not os.walk
# hint: to implement os.walk read about DFS and recursion

# CR: create a class named DirectoryTraversal or something like that organize the code
# DirectoryTraversal(path: string)
# count_files() -> int
import os.path

class DirectoryTraversal:

    def __init__(self, path) -> None:
        self.path = path    #instance variable

    def count_files(self, path) -> int:
        file_count: int = 0
        files = os.listdir(path)
        for i in range(len(files)):
            path_in_path: str = os.path.join(path, files[i])
            if os.path.isdir(path_in_path):
                file_count += self.count_files(path_in_path)
            else:
                file_count += 1

        return file_count

path1: str = input("Give a path: ")
path2: str = input("Give another path: ")

d1: object = DirectoryTraversal(path1)
d2: object = DirectoryTraversal(path2)
count1: int = d1.count_files(path1)
count2: int = d2.count_files(path2)
print("path1 has: " + str(count1) + " files")
print("path2 has: " + str(count2) + " files")

if count1 > count2:
    print("path1 has more files")
elif count1 == count2:
    print("both paths have the same amount of files")
else:
    print("path2 has more files")
