import os
import json

def generate_file_list():
    file_dict = {}
    count = 0

    # Walk through all the files in the repository directory.
    for root, dirs, files in os.walk("."):
        for file in files:
            # Skip hidden files or Git files or Python files
            if file.startswith('.') or '.git' in root or file.endswith(".py"):
                continue
            file_dict[f"s{str(count).zfill(3)}"] = file
            count += 1

    # Write the file list to a JSON file
    with open("strudel.json", "w") as f:
        json.dump(file_dict, f, indent=4)

if __name__ == "__main__":
    generate_file_list()
