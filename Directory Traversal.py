# input: two directory paths
# output: print which directory has more files (recursively)
# notes: you can use os.listdir and os.path.isdir but not os.walk
# hint: to implement os.walk read about DFS and recursion

# CR: after fixing a Cr remove it, unless you are not sure if it's fixed
# CR: create a class named DirectoryTraversal or something like that organize the code
# DirectoryTraversal(path: string)
# count_files() -> int
import os.path

# CR: move this class to a separate module (named after the class). You can read about python modules and files
class DirectoryTraversal:
    path: str = "" # CR: type is optional for inline variables (I like it but just so you know it's less important)
    def __init__(self, path) -> None: # CR: path should be typed
        self.path = path    #instance variable
        
        
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
    
    # CR: Move all of this (below) code to a function (e.g. compare_two_paths_file_count) in a static Main class 
path1: str = input("Give a path: ")
path2: str = input("Give another path: ")

d1: object = DirectoryTraversal(path1)
d2: object = DirectoryTraversal(path2)
count1: int = d1.count_files()
count2: int = d2.count_files()
print("path1 has: " + str(count1) + " files")
print("path2 has: " + str(count2) + " files")

# CR: merge the three prints with a single one: f"Path {path1} has {count1} files and path {path2} has {count2} files"
if count1 > count2:
    print("path1 has more files")
elif count1 == count2:
    print("both paths have the same amount of files")
else:
    print("path2 has more files")

    # CR: the next next will be to print the files instead of counting them. After that I want you to try to think how to implement it without recursion (a little hard).
