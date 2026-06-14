from flask import Flask, render_template, request, jsonify
import json

from modules.rag import answer_question

app = Flask(__name__)

with open("generated/summaries.json", "r", encoding="utf-8") as f:
    summaries = json.load(f)

with open("generated/extracted_info.json", "r", encoding="utf-8") as f:
    extracted = json.load(f)


@app.route("/")
def home():

    topics = []

    for topic in summaries:

        topics.append({
            "name": topic,
            "summary": summaries[topic][:150] + "..."
        })

    return render_template("home.html", topics=topics)


@app.route("/topic/<topic_name>")
def topic_page(topic_name):

    return render_template(
        "topic.html",
        topic=topic_name,
        summary=summaries[topic_name],
        data=extracted[topic_name]
    )


@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    question = data["question"]

    result = answer_question(question)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)