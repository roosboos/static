import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_equal_nodes(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)
    
    def test_not_equal_due_to_text(self):
        node = TextNode("ooga booga", TextType.IMAGE)
        node2 = TextNode("dingy pingy", TextType.IMAGE)
        self.assertNotEqual(node, node2)
    
    def test_not_equal_due_to_text_type(self):
        node = TextNode("oh yeah", TextType.LINK)
        node2 = TextNode("oh yeah", TextType.BOLD)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()