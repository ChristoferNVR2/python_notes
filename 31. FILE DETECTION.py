import os

path = "C:\\Users\\LENOVO\\Desktop\\test.txt"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")

else:
    print("That location doesn't exist!")

path2 = "C:\\Users\\LENOVO\\Desktop\\folder"

if os.path.exists(path2):
    print("That location exists!")
    if os.path.isfile(path2):
        print("That is a file")
    elif os.path.isdir(path2):
        print("That is a directory")
else:
    print("That location doesn't exist!")
