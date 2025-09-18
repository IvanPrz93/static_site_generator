import os

from markdown_blocks import markdown_to_html_node, extract_title


def generate_page_recursively(source, template, destination):
    
    dir = os.listdir(source)

    for item in dir:
        full_source_path = os.path.join(source, item)

        full_destination_path = os.path.join(destination, item)

        if os.path.isfile(full_source_path):
            destination_path, md_ext = os.path.splitext(full_destination_path)
            full_destination_path = destination_path + ".html"
            generate_page(full_source_path, template, full_destination_path) 
            print(f"Succesfully copied {item} in {destination}")
        if os.path.isdir(full_source_path):
            os.makedirs(full_destination_path)
            print(f"Succesfully created {full_destination_path} directory")
            generate_page_recursively(full_source_path, template, full_destination_path)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown_file_string = f.read()
    with open(template_path, "r") as t:
        template_file_string = t.read()
    
    html_node = markdown_to_html_node(markdown_file_string)
    html_string = html_node.to_html()
    title = extract_title(markdown_file_string)

    template = template_file_string.replace("{{ Title }}", title).replace("{{ Content }}", html_string)

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))

    with open(dest_path, "w") as d:
        d.write(template)
    print(f'Successfully wrote to "{dest_path}" ({len(template)} characters written)')
    
