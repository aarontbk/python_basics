# input: two directory paths
# output: print which directory has more files (recursively)
# notes: you can use os.listdir and os.path.isdir but not os.walk
# hint: to implement os.walk read about DFS and recursion


import os.path

path1 = input("Give a path: ")
path2 = input("Give another path: ")

def count_files(path):
    global file_count
    file_count = 0
    files = os.listdir(path)
    for i in range(len(files)):
        if os.path.isdir(path + "\\" + files[i]):
            file_count += count_files(path + "\\" + files[i])
        else:
            file_count += 1

    return file_count


file_count1 = count_files(path1)
file_count2 = count_files(path2)
print("path1 has: " + str(file_count1) + " files")
print("path2 has: " + str(file_count2) + " files")

if file_count1 > file_count2:
    print("path1 has more files")
elif file_count1 == file_count2:
    print("both paths have the same amount of files")
else:
    print("path2 has more files")
