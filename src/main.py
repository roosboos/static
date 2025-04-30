import os
import shutil

from copystatic import copy_static
from gencontent import generate_page


def main():
    print("Copying static files")
    copy_static("/home/johnr/static/static",  "/home/johnr/static/public")
    print("Static files copied successfully!")

    generate_page("content/index.md", "template.html", "public/index.html")
    generate_page("content/blog/glorfindel/index.md", "template.html", "public/blog/glorfindel/index.html")
    generate_page("content/blog/tom/index.md", "template.html", "public/blog/tom/index.html")
    generate_page("content/blog/majesty/index.md", "template.html", "public/blog/majesty/index.html")
    generate_page("content/contact/index.md", "template.html", "public/contact/index.html")



main()
