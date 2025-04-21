import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html_with_href(self):
        # Create a node with href property
        node = HTMLNode("a", "Click me", None, {"href": "https://example.com"})
        # Check if props_to_html returns the correct string
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')
    
    def test_props_to_html_with_multiple_props(self):
        # Create a node with multiple properties
        node = HTMLNode(
            "a", 
            "Click me", 
            None, 
            {
                "href": "https://example.com", 
                "target": "_blank", 
                "class": "link"
            }
        )
        # The order of properties might vary, so we check for each property separately
        result = node.props_to_html()
        self.assertIn(' href="https://example.com"', result)
        self.assertIn(' target="_blank"', result)
        self.assertIn(' class="link"', result)
        # Check the total length to ensure nothing extra is there
        expected_length = len(' href="https://example.com" target="_blank" class="link"')
        self.assertEqual(len(result), expected_length)
    
    def test_props_to_html_with_no_props(self):
        # Create a node with no properties
        node = HTMLNode("p", "Hello, world!", None, None)
        # Check if props_to_html returns an empty string
        self.assertEqual(node.props_to_html(), "")
        
        # Also test with empty dict
        node = HTMLNode("p", "Hello, world!", None, {})
        self.assertEqual(node.props_to_html(), "")
    
    def test_repr_method(self):
        # Test that __repr__ outputs something reasonable
        node = HTMLNode("div", "Content", None, {"class": "container"})
        repr_str = repr(node)
        # Check that the representation includes key information
        self.assertIn("div", repr_str)
        self.assertIn("Content", repr_str)
        self.assertIn("container", repr_str)

if __name__ == "__main__":
    unittest.main()