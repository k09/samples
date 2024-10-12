import os
import json

def generate_file_list():
    file_dict = {}

    # Walk through all the files in the repository directory.
    file_dict[f"_base"] = "https://raw.githubusercontent.com/k09/samples/refs/heads/master/"
    for root, dirs, files in os.walk("."):
        for file in files:
            # Check if file does not end with .wav or .mp3
            if not file.endswith(('.wav', '.mp3')):
                continue
            file_dict[Path(file).stem] = file

    # Write the file list to a JSON file
    with open("strudel.json", "w") as f:
        json.dump(file_dict, f, indent=4)

if __name__ == "__main__":
    generate_file_list()
