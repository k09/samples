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
    
    #with open("strudel.json", "w") as f:
    #    json.dump(wrapped_dict, f, indent=4)

    # Generate the JSON string with double quotes
    json_str = json.dumps(file_dict, indent=4)

    # Custom modifications:
    # 1. Remove the quotes around keys (this is dangerous but can work for basic dictionaries)
    # 2. Replace double quotes with single quotes for the values
    json_str_custom = json_str.replace('"', "'")  # Replace all double quotes with single quotes
    #json_str_custom = json_str_custom.replace("'samples': {", "samples: {")  # Remove quotes from the key

    # More advanced regex could be used if needed for more control over formatting
    wrapped_dict = {"samples": json_str_custom}
    # Write to file
    with open("strudel.json", "w") as f:
        json.dump(wrapped_dict, f, indent=4)



if __name__ == "__main__":
    generate_file_list()
