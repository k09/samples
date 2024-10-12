import os
import json
from pathlib import Path

def generate_file_list():
    file_dict = {}
    file_dict[f"_base"] = "https://raw.githubusercontent.com/k09/samples/main/"
    for root, dirs, files in os.walk("."):
        for file in files:
            if not file.endswith(('.wav', '.mp3')):
                continue
            file_dict[Path(file).stem] = [file]
    with open("strudel.json", "w") as f:
        json.dump(file_dict, f, indent=4)

if __name__ == "__main__":
    generate_file_list()
