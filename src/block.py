from enum import Enum

def markdown_to_blocks(markdown):
    fixed_markdown_list = []
    fixed_markdown = markdown.split("\n\n")
    for fix in fixed_markdown:
        new_value = fix.strip()
        if new_value:
            fixed_markdown_list.append(new_value)
    return fixed_markdown_list

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if block.startswith('#'):
        i = 0
        while i < len(block) and block[i] == '#':
            i += 1
        if 1 <= i <= 6 and i < len(block) and block[i] == ' ':
            return BlockType.HEADING
    
    if block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    
    lines = block.split("\n")
    
    # Check if ALL lines start with '>'
    if all(line.startswith('>') for line in lines):
        return BlockType.QUOTE
    
    # Check if ALL lines start with '- '
    if all(line.startswith('- ') for line in lines):
        return BlockType.UNORDERED_LIST
    
    is_ordered_list = True
    for i, line in enumerate(lines, 1):
        if not line.startswith(f"{i}. "):
            is_ordered_list = False
            break
    if is_ordered_list and lines:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH