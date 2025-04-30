import os 
import shutil

def copy_static(source_dir, dest_dir):
    if os.path.exists(dest_dir):
        print(f"Removing existing directory: {dest_dir}")
        shutil.rmtree(dest_dir)
    
    print(f"Creating directory: {dest_dir}")
    os.mkdir(dest_dir)

    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)

        if os.path.isfile(source_path):
            print(f"Copying file: {source_path} -> {dest_path}")
            shutil.copy(source_path, dest_path)
        elif os.path.isdir(source_path):
            print(f"Copying directory: {source_path} -> {dest_path}")
            os.mkdir(dest_path)
            copy_static(source_path, dest_path)
        else: 
            print(f"Skipping: {source_path} (not a file or directory)")