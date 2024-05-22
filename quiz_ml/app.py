# flask
from flask import Flask, render_template, request, redirect, url_for, make_response

"""
с помощью __name__ указываем, что app.py основной файл
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
