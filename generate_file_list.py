import os
import json

def generate_file_list():
    file_dict = {}
    count = 0

    # Walk through all the files in the repository directory.
    for root, dirs, files in os.walk("."):
        for file in files:
            # Check if file does not end with .wav or .mp3
            if not file.endswith(('.wav', '.mp3')):
                continue
            file_dict[f"s{str(count).zfill(3)}"] = file
            count += 1

    # Write the file list to a JSON file
    wrapped_dict = {"samples": file_dict}
    with open("strudel.json", "w") as f:
        json.dump(wrapped_dict, f, indent=4)

if __name__ == "__main__":
    generate_file_list()
