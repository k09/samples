import os
import json

def generate_file_list():
    file_dict = {}
    count = 0
    for root, dirs, files in os.walk("."):
        for file in files:
            if not file.endswith(('.wav', '.mp3')):
                continue
            file_dict[f"s{str(count).zfill(3)}"] = file
            count += 1
    json_str = "\"samples\": {\n"
    for key, value in file_dict.items():
        json_str += f"    {key}: '{value}',\n"
    json_str = json_str.rstrip(",\n") + "\n}"

    with open("strudel.json", "w") as f:
        f.write(json_str)

if __name__ == "__main__":
    generate_file_list()
