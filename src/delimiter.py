from textnode import TextType, TextNode
import re

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

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]+)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        # Start with the remaining text to process
        remaining_text = old_node.text

        # Continue processing while an "image" markdown is found
        while "![" in remaining_text:
            # Locate the image alt text
            index_start = remaining_text.find("![")
            start_alt = index_start + 2
            end_alt = remaining_text.find("]", start_alt)
            alt_text = remaining_text[start_alt:end_alt]

            # Locate the image URL
            start_url = remaining_text.find("(", end_alt) + 1
            end_url = remaining_text.find(")", start_url)
            url_text = remaining_text[start_url:end_url]

            # Split the text into "before image" and "after image"
            text_before = remaining_text[:index_start]
            remaining_text = remaining_text[end_url + 1:]

            # Append `text_before` as a TextNode (if there is text before)
            if text_before:
                new_nodes.append(TextNode(text_before, TextType.TEXT))

            # Append the image as a TextNode
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url_text))

        # Append any remaining text as a TextNode (if it exists)
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        # Start processing the node's text to extract links
        remaining_text = old_node.text

        while "[" in remaining_text:
            # Find the start and end of the link text
            index_start = remaining_text.find("[")
            link_text_start = index_start + 1
            link_text_end = remaining_text.find("]", link_text_start)
            link_text = remaining_text[link_text_start:link_text_end]

            # Find the start and end of the link URL
            link_url_start = remaining_text.find("(", link_text_end) + 1
            link_url_end = remaining_text.find(")", link_url_start)
            link_url = remaining_text[link_url_start:link_url_end]

            # Extract text before the link
            text_before = remaining_text[:index_start]

            # Extract remaining text after the link
            remaining_text = remaining_text[link_url_end + 1:]

            # Append 'text_before' (if not empty) as a TextNode
            if text_before:
                new_nodes.append(TextNode(text_before, TextType.TEXT))

            # Append the extracted link as a TextNode
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

        # Once no more links are found, append the leftover remaining text (if any)
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes


