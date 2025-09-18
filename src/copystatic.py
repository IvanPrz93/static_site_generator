import os, shutil


def copy_files(source, destination):
    
    dir = os.listdir(source)

    for item in dir:
        full_source_path = os.path.join(source, item)

        full_destination_path = os.path.join(destination, item)

        if os.path.isfile(full_source_path):
            shutil.copy(full_source_path, full_destination_path) 
            print(f"Succesfully copied {item} in {destination}")
        if os.path.isdir(full_source_path):
            os.makedirs(full_destination_path)
            print(f"Succesfully created {full_destination_path} directory")
            copy_files(full_source_path, full_destination_path)

