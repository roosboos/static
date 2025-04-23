from textnode import *
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # Store our result nodes
    result_nodes = []
    
    for old_node in old_nodes:
        # Non-TEXT nodes pass through unchanged
        if old_node.text_type != TextType.TEXT:
            result_nodes.append(old_node)
            continue
            
        text = old_node.text
        first_pos = text.find(delimiter)
        
        # No delimiter? Keep node as-is
        if first_pos == -1:
            result_nodes.append(old_node)
            continue
            
        # Find closing delimiter
        second_pos = text.find(delimiter, first_pos + len(delimiter))
        if second_pos == -1:
            raise ValueError(f"No matching closing delimiter: {delimiter}")
        
        # Split into three parts
        before = text[:first_pos]
        middle = text[first_pos + len(delimiter):second_pos]
        after = text[second_pos + len(delimiter):]
        
        # Add "before" text if it exists
        if before:
            result_nodes.append(TextNode(before, TextType.TEXT))
        
        # Add the formatted middle text
        result_nodes.append(TextNode(middle, text_type))
        
        # Recursively process any remaining text
        if after:
            after_node = TextNode(after, TextType.TEXT)
            # This is key: recursively process the rest of the text
            after_nodes = split_nodes_delimiter([after_node], delimiter, text_type)
            result_nodes.extend(after_nodes)
    
    return result_nodes