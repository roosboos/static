from textnode import TextNode, TextType

def main():
    node = TextNode("lmaoooo", TextType.LINK, "https://youtube.com")

    print(node)

if __name__ == "__main__":
    main()