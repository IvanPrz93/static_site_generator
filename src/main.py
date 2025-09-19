import os, shutil, sys
from copystatic import copy_files
from gencontent import generate_page_recursively


source = "static"
destination = "docs"
content = "content"


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.makedirs(destination)

    print(f"Copying {source} files to {destination} directory...")
    copy_files(source, destination)

    generate_page_recursively(content, "template.html", destination, basepath)


main()
