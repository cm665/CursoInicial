import os

path = "c:\\users\\cakow\\desktop\\folder"

if os.path.exists(path):
    print("that location exists")
    if os.path.isfile(path):
        print("that is a file")
    elif os.path.isdir(path):
        print("that ia a directory!")
else:
    print("that location doesn´t exist")