from textnode import TextNode, TextType
from htmlnode import *
from delimiter import *

def main():
    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])

    print(new_nodes)


if __name__ == "__main__":
    main()