import os
import json
from modules.extractor import extract_information

DATA_FOLDER = "data"

all_extractions = {}

for file in os.listdir(DATA_FOLDER):

    if file.endswith(".txt"):

        print(f"Processing {file}...")

        path = os.path.join(DATA_FOLDER, file)

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        topic = os.path.splitext(file)[0]

        extracted_data = extract_information(text)

        all_extractions[topic] = extracted_data

        print(f"Completed {topic}")

os.makedirs("generated", exist_ok=True)

with open("generated/extracted_info.json", "w", encoding="utf-8") as f:

    json.dump(
        all_extractions,
        f,
        indent=4,
        ensure_ascii=False
    )

print("Extraction completed!")