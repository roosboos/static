import unittest
from block import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class TestMarkdownBlockTypes(unittest.TestCase):

    def test_paragraph(self):
        test_cases = [
            "This is a simple paragraph.",
            "This is a paragraph\nwith multiple lines.",
            "Just some text without any special markers."
        ]
        for case in test_cases:
            with self.subTest(case=case):
                self.assertEqual(block_to_block_type(case), BlockType.PARAGRAPH)
    
    def test_heading(self):
        test_cases = [
            ("# Heading 1", BlockType.HEADING),
            ("## Heading 2", BlockType.HEADING),
            ("### Heading 3", BlockType.HEADING),
            ("#### Heading 4", BlockType.HEADING),
            ("##### Heading 5", BlockType.HEADING),
            ("###### Heading 6", BlockType.HEADING),
            ("####### Too many #s", BlockType.PARAGRAPH),
            ("#No space after #", BlockType.PARAGRAPH)
        ]
        for case, expected in test_cases:
            with self.subTest(case=case):
                self.assertEqual(block_to_block_type(case), expected)

if __name__ == "__main__":
    unittest.main()