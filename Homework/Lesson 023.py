import os


def scan_directory(root):

    for i in os.listdir(root):
        size_file = os.path.getsize(fr"{root}\{i}")

        if os.path.isfile(fr"{root}\{i}"):
            print(f"{i} - file - {size_file} bytes")
        else:
            print(f"{i} - dir")


scan_directory(r"..\..\..\Abstract")
