

# input: two directory paths
# output: print which directory has more files (recursively)
# notes: you can use os.listdir and os.path.isdir but not os.walk
# hint: to implement os.walk read about DFS and recursion


import os.path

file_count1 = 0
file_count2 = 0

path1 = input("Give a path: ")
path2 = input("Give another path: ")

def count_files(file_count, path):
    dir = os.listdir(path)
    for i in dir (len(dir)):
        if os.path.isfile(path + r"\"" + i):
            file_count += 1
        else:
            count_files(file_count, os.listdir(path + r"\"" + i), dir)
    return file_count

first = count_files(file_count1, path1)
second = count_files(file_count2, path2)

if file_count1 > file_count2:
    print(path1 + "   --->  has more files")
elif file_count1 == file_count2:
    print("both paths have: " + file_count1 + " files")
else:
    print(path2 + "   --->  has more files")