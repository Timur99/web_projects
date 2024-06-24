
'''
# flask
from flask import Flask, render_template, request, redirect, url_for, make_response

"""
с помощью __name__ указываем, что mistral.py основной файл
"""
app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static',
)


@app.route('/')  # какой url нужно отслеживать
def index():
    return render_template('index.html')

if __name__ == '__main__':  # если данный файл будет основным файлом для запуска
    app.run(debug=True)     # True ошибки будут выводиться на сайте, чтобы ошибки не показывались на сайте - False

'''
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
    return render_template('mistral.html')

@app.route('/process_text', methods=['POST'])
def process_text_route():
    # Получаем текст из запроса
    text = request.json['text']

    # Передаем текст в функцию process_text
    result = process_text(text)

    # Возвращаем результат в формате JSON
    return jsonify(result=result)

def process_text(text):
    api_key = "Yn9KHMe1ZlbNf85LVemsr7J16lHpGjPL"
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
