import os

source = "C:\\Users\\LENOVO\\Desktop\\folder\\hola.txt"
destination = "D:\\PYTHON\\PythonBroC\\text.py"

try:
    if os.path.exists(destination):
        print("File already exists")
    else:
        os.replace(source, destination)
        print(source + "was moved")
except FileNotFoundError:
    print(source + "was not found")

# You only can move the file while the source and the destination are in the same disk partition
# If you want to execute this code, you need to change the source and destination path
# This will be the output:
# Traceback (most recent call last):
#   File "D:\PYTHON\PythonBroC\dev.py", line 10, in <module>
#     os.replace(source, destination)
# OSError: [WinError 17] El sistema no puede mover el archivo a otra unidad de disco: 'C:\\Users\\LENOVO\\Desktop\\folder\\hola.txt' -> 'D:\\PYTHON\\PythonBroC\\text.py'

# this is another example of moving a file successfully

source_ = "test.txt"
destination_ = "D:\\PYTHON\\text.py"

try:
    if os.path.exists(destination_):
        print("File already exists")
    else:
        os.replace(source_, destination_)
        print(source_ + "was moved")
except FileNotFoundError:
    print(source_ + "was not found")
