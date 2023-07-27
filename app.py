import openai
from flask import Flask, request, jsonify, render_template, Response
import requests
import json

app = Flask(__name__)

openai.api_key="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"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    messages = request.form.get("user_input", None)
    if messages is None:
        return jsonify({"error": {"message": "请输入prompts！", "type": "invalid_request_error", "code": ""}})

    # json串转对象
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": messages}]
    )
    reply=completion['choices'][0]['message']['content'].strip()

    return render_template('index.html', user_input=messages, reply=reply)

if __name__ == '__main__':
    app.run(port=5000)
