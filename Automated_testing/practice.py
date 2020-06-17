import os
def GetDesktopPath():
    return os.path.join(os.path.expanduser("~"), 'Desktop')
a = GetDesktopPath()
print(a)