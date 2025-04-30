import os
from pathlib import Path
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

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    entries = os.listdir(dir_path_content)
    for entry in entries:
        source_path = os.path.join(dir_path_content, entry)
        if os.path.isfile(source_path):
            if entry.endswith(".md"):
                content_path = Path(dir_path_content)
                source_path = Path(dir_path_content) / entry

                relative_path = source_path.relative_to(content_path)

                html_path = relative_path.with_suffix('.html')

                dest_path = Path(dest_dir_path) / html_path

                dest_path.parent.mkdir(parents=True, exist_ok =True)

                generate_page(str(source_path), template_path, str(dest_path))
        elif os.path.isdir(source_path):
            new_dest_dir = os.path.join(dest_dir_path, entry)
            generate_pages_recursive(source_path, template_path, new_dest_dir)