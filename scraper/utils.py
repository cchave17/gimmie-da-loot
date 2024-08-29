import os
import json

def create_article_directory(base_dir, article_title, index):
    # Create folder name with underscores for spaces and pagination
    folder_name = f"{index}_{article_title.replace(' ', '_')}"
    folder_path = os.path.join(base_dir, folder_name)

    # Create the directory and assets subfolder
    os.makedirs(os.path.join(folder_path, 'assets'), exist_ok=True)

    return folder_path

def save_metadata(folder_path, metadata):
    with open(os.path.join(folder_path, 'metadata.json'), 'w') as file:
        json.dump(metadata, file, indent=4)
