# input: two directory paths
# output: print which directory has more files (recursively)
# notes: you can use os.listdir and os.path.isdir but not os.walk
# hint: to implement os.walk read about DFS and recursion


import os.path

Folders_to_verify = []
file_count = 0
path1 = input("Give a path: ")
path2 = input("Give another path: ")

def count_files(path):
    global file_count, Folders_to_verify
    files = [os.path.splitext(filename)[0] for filename in os.listdir(path)]
    for i in range(len(files)):
        if os.path.isdir(path + r"\"" + files[i]):
            Folders_to_verify.append(path + r"\"" + files[i])
        else:
            file_count += 1

    for k in range(len(Folders_to_verify)):
        count_files(Folders_to_verify[k])

    return file_count


file_count1 = count_files(path1)
file_count = 0
file_count2 = count_files(path2)

if file_count1 > file_count2:
    print(path1 + "   --->  has more files")
elif file_count1 == file_count2:
    print("both paths have: " + str(file_count1) + " files")
else:
    print(path2 + "   --->  has more files")
