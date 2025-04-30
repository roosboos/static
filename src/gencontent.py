import os
from markdown_blocks import markdown_to_html_node

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("Not a title")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r") as file:
        from_file_content = file.read()
    
    with open(template_path, "r") as file:
        template_file_content = file.read()
    
    html_node = markdown_to_html_node(from_file_content)
    html_content = html_node.to_html()

    extracted = extract_title(from_file_content)

    final_html = template_file_content.replace("{{ Title }}", extracted)
    final_html = final_html.replace("{{ Content }}", html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(final_html)