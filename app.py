import openai
from flask import Flask, request, jsonify, render_template, Response
import requests
import json
import os

app = Flask(__name__)

# 从配置文件中settings加载配置
app.config.from_pyfile('settings.py')
openai.api_key = os.environ.get('OPENAI_API_KEY',app.config["OPENAI_API_KEY"])

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
