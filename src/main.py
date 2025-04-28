from textnode import TextNode,TextType
from htmlnode import *
from delimiter import *

def main():
    example_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    result = text_to_textnodes(example_text)
    print(result)

if __name__ == "__main__":
    main()