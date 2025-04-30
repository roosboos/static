import os
import shutil

from copystatic import copy_static


def main():
    print("Copying static files")
    copy_static("/home/johnr/static/static",  "/home/johnr/static/public")
    print("Static files copied successfully!")

main()
