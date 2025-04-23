from textnode import TextNode, TextType
from htmlnode import *
from delimiter import *

def main():
    text = """Here's an image:
    ![alt text](https://example.com/image.png)
    And here's a link:
    [Link Text](https://example.com)
    """
    print(extract_markdown_images(text))  # What do you expect here?
    print(extract_markdown_links(text))


if __name__ == "__main__":
    main()