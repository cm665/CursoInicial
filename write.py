import os



path = "hola.txt"

try:
    os.remove(path)
except FileNotFoundError:
    print("that file was not found")
except PermissionError:
    print("you do not have permission to delete that")
except OSError:
    print("you cannot delete that using that function")
else:
    print(path+" was deleted")