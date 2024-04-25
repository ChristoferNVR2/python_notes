import os
import shutil

path = "test.txt"

try:
    os.remove(path)
except FileNotFoundError:
    print("That file was not found")

path2 = "empty_folder"

try:
    # os.remove(path_)
    os.rmdir(path2)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
else:
    print(path2 + " was deleted successfully")

path3 = "folder"

try:
    # os.rmdir(path3)
    shutil.rmtree(path3)  # This method deletes the folder and all its contents
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete a folder that is not empty")
else:
    print(path3 + " was deleted successfully")
