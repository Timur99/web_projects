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
    """
    api_key: API токен от Mistral
    model: версия модели
    """

    def get_api_key_from_file(filename):
        try:
            with open(filename, 'r') as file:
                api_key = file.read().strip()
            return api_key
        except FileNotFoundError:
            print(f"File {filename} not found.")
            return None

    # Использование функции
    filename = "api_key.txt"
    api_key = get_api_key_from_file(filename) #
    #api_key = ""
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
