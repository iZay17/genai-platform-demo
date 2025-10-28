from flask import Flask, request, jsonify
from datetime import datetime
import openai, os, csv

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "Hello, world!")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    output = response.choices[0].message["content"]

    # Log prompt and timestamp for governance/auditing
    with open("audit_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), prompt, len(prompt), len(output)])

    return jsonify({"response": output})

if __name__ == "__main__":
    app.run(debug=True)
