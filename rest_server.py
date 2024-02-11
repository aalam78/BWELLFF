from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

@app.route('/chat', methods=['POST'])
def chat_with_gpt():
    data = request.json
    prompt = data.get('prompt', '')
    response = client.completions.create(model="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=50)
    chat_response = response.choices[0].text.strip()
    return jsonify({'response': chat_response})

@app.route('/')
def index():
    return 'Welcome to the ChatGPT API!'

@app.route('/favicon.ico')
def favicon():
    return '', 404

if __name__ == "__main__":
    app.run(debug=True, port=5001)
