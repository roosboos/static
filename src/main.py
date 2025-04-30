import os
import shutil

from copystatic import copy_static
from gencontent import generate_page, generate_pages_recursive


def main():
    print("Copying static files")
    copy_static("/home/johnr/static/static",  "/home/johnr/static/public")
    print("Static files copied successfully!")

    print("Generating pages")
    generate_pages_recursive("/home/johnr/static/content", "/home/johnr/static/template.html", "/home/johnr/static/public")
    print("Pages generated successfully!")

    
    



main()
