import unittest
from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter

class DelimiterTest(unittest.TestCase):
    def test_no_delimiters(self):
        node = TextNode("Plain text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "Plain text")
    
    def test_bold(self):
        node = TextNode("Text with **bold** word", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
    
    def test_code(self):
        node = TextNode("Code `snippet` here", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result[1].text, "snippet")
        self.assertEqual(result[1].text_type, TextType.CODE)
    
    def test_italic(self):
        node = TextNode("Some _italic_ text", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(result[1].text_type, TextType.ITALIC) 
    
    def test_error(self):
        node = TextNode("Unclosed **bold", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD) 

if __name__ == "__main__":
    unittest.main()
    