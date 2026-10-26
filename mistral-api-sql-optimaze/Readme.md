# mistral-api-sql-optimaze

Flask-приложение с текстовым полем и ответами Mistral. Его можно использовать для запросов об оптимизации SQL, но код отправляет введённый текст как обычное сообщение модели: подключения к базе и выполнения SQL здесь нет.

## Быстрый запуск

Из корня репозитория:

```bash
cd mistral-api-sql-optimaze
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install Flask 'mistralai==0.4.2'
python -m flask --app main_mistral run --host 127.0.0.1 --port 5000
```

Откройте [интерфейс](http://127.0.0.1:5000/). Без ключа можно открыть страницу и выполнить локальную проверку ниже. Для реального запроса создайте в папке проекта файл `token.txt` и сохраните в нём только свой ключ Mistral API. Файл исключён из Git; приложение читает его относительно рабочей папки. Остановить сервер: `Ctrl+C`.

Код использует старые `MistralClient` и `ChatMessage`, поэтому для него указана версия [mistralai 0.4.2](https://pypi.org/project/mistralai/0.4.2/). Файл `requiremnts.txt` в репозитории назван с опечаткой, не содержит Flask и не фиксирует версию SDK; для текущего кода используйте команду установки выше.

## Как проверить без ключа и внешнего API

Из папки проекта в активном окружении; запущенный сервер не нужен:

```bash
python - <<'PY'
from unittest.mock import patch
from main_mistral import app
with app.test_client() as client:
    assert client.get('/').status_code == 200
    with patch('main_mistral.process_text', return_value='Тестовый ответ') as process:
        response = client.post('/process_text', json={'text': 'SELECT 1;'})
        assert response.status_code == 200
        assert response.get_json() == {'result': 'Тестовый ответ'}
        process.assert_called_once_with('SELECT 1;')
print('Страница и обработчик запроса работают')
PY
```

Эта проверка подменяет вызов модели и проверяет только локальное приложение.

## Проверка реального ответа

После добавления ключа и запуска сервера введите в браузере `Объясни SQL-запрос SELECT 1;` и нажмите «Отправить». Под полем должен появиться ответ модели. Запрос передаётся в Mistral и может расходовать средства API-аккаунта.

Реальный ответ зависит от действующего ключа, доступа к модели `mistral-large-latest` и совместимости старого SDK с API. Обработка ошибок API в приложении не реализована: при сбое смотрите вывод сервера и вкладку Network в инструментах разработчика браузера.

