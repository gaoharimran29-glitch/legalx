import json
import os

from gtts import gTTS

os.makedirs("audio",exist_ok=True)

with open("generated/summaries.json", "r", encoding="utf-8") as f:

    summaries = json.load(f)

for topic, summary in summaries.items():

    tts = gTTS(text=summary, lang="en")

    tts.save(f"audio/{topic}.mp3")

    print(f"Generated audio for {topic}")