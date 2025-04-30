import os
import shutil

from copystatic import copy_static
from gencontent import generate_page


def main():
    print("Copying static files")
    copy_static("/home/johnr/static/static",  "/home/johnr/static/public")
    print("Static files copied successfully!")

    generate_page("content/index.md", "template.html", "public/index.html")



main()
