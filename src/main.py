import os, shutil
from copystatic import copy_files
from gencontent import generate_page_recursively


source = "static"
destination = "public"


def main():
    if os.path.exists(destination):
        shutil.rmtree(destination)
        print(f"Succesfully deleted {destination} directory")
    os.makedirs(destination)
    print(f"Succesfully created {destination} directory")

    print(f"Copying {source} files to {destination} directory...")
    copy_files(source, destination)

    generate_page_recursively("content", "template.html", "public")


main()
