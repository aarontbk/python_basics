

# input: two directory paths
# output: print which directory has more files (recursively)
# notes: you can use os.listdir and os.path.isdir but not os.walk
# hint: to implement os.walk read about DFS and recursion


import os.path

path1 = input("Give a path: ")
path2 = input("Give another path: ")
file_count1 = sum(len(files) for _, _, files in os.walk(path1))
file_count2 = sum(len(files) for _, _, files in os.walk(path2))

if file_count1 > file_count2:
    print(path1 + "   --->  has more files")
elif file_count1 == file_count2:
    print("both paths have: " + file_count1 + " files")
else:
    print(path2 + "   --->  has more files")