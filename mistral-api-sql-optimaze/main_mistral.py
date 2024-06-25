from flask import Flask, request, jsonify, render_template
import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static',
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_text', methods=['POST'])
def process_text_route():
    # Получаем текст из запроса
    text = request.json['text']
    result = process_text(text)
    return jsonify(result=result)

def process_text(text):
    api_key = "" #тут нужен API токен от Mistral
    model = "mistral-large-latest"

    client = MistralClient(api_key=api_key)

    chat_response = client.chat(
        model=model,
        messages=[ChatMessage(role="user", content=text)]
    )

    print(chat_response.choices[0].message.content)
    return chat_response.choices[0].message.content

if __name__ == '__main__':
    app.run(debug=True)
