import os
from extraction import extract_title
from blocks import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_path = os.path.abspath(from_path)
    template_path = os.path.abspath(template_path)


    with open(from_path, "r") as f:
        md_file = f.read()

    with open(template_path, "r") as t:
        template = t.read()

    html_string = markdown_to_html_node(md_file).to_html()
    title = extract_title(md_file)
    new_template = template.replace("{{ Title }}", title)
    new_template = new_template.replace("{{ Content }}", html_string)
    dest_dir = os.path.dirname(dest_path)

    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as g:
        g.write(new_template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for file in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, file)
        temp_path = os.path.abspath(template_path)
        print(os.path.isfile(src_path), src_path, type(src_path))
        if os.path.isfile(src_path):
            rel_path = os.path.relpath(src_path, dir_path_content)
            dest_path = os.path.join(dest_dir_path, rel_path).replace(".md", ".html")
            print(f"File Path: {src_path}\nTemplate Path: {temp_path}\nDestination Path: {dest_path}")
            generate_page(src_path, temp_path, dest_path)
        else:
            rel_path = os.path.relpath(src_path, dir_path_content)
            dest_subdir = os.path.join(dest_dir_path, rel_path)
            print(f"Checking Dir: {src_path}\n")
            if os.path.isdir(dest_subdir):
                generate_pages_recursive(src_path, temp_path, dest_subdir)
            else:
                os.makedirs(dest_subdir, exist_ok=True)
                generate_pages_recursive(src_path, temp_path, dest_subdir)


# generate_pages_recursive("content", "template.html", "public/index.html")