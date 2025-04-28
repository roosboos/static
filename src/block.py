def markdown_to_blocks(markdown):
    fixed_markdown_list = []
    fixed_markdown = markdown.split("\n\n")
    for fix in fixed_markdown:
        new_value = fix.strip()
        if new_value:
            fixed_markdown_list.append(new_value)
    return fixed_markdown_list