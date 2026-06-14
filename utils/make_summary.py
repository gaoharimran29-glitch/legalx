import os
import json
from modules.summarizer import generate_summary

DATA_FOLDER = "data"
OUTPUT_FILE = "generated/summaries.json"

all_summaries = {}

for file in os.listdir(DATA_FOLDER):

    if file.endswith(".txt"):

        file_path = os.path.join(DATA_FOLDER, file)

        print(f"Processing {file}...")

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        summary = generate_summary(text)

        topic_name = os.path.splitext(file)[0]

        all_summaries[topic_name] = summary

        print(f"Completed {topic_name}")


os.makedirs("generated", exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(
        all_summaries,
        f,
        indent=4,
        ensure_ascii=False
    )

print("All summaries saved successfully!")