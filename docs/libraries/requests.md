# Requests

[Requests](https://docs.python-requests.org/) — это одна из самых популярных библиотек для выполнения HTTP-запросов в Python. Она позволяет легко отправлять GET и POST-запросы, работать с параметрами, заголовками, JSON и форм-данными.

---

## Установка

Установить библиотеку можно через pip:

```bash
pip install requests
```

Либо же через Anaconda:

```bash
conda install requests
```

---

## Примеры использования

Файл [requests_example.py](../../src/libraries/requests_example.py) демонстрирует базовые и полезные сценарии работы с HTTP-запросами с помощью `requests`. Ниже приведён разбор каждого примера.

> ⚠️ **Важно:** Для успешного запуска примеров требуется доступ в интернет.

---

### 1. Выполнение GET-запроса

```python
import requests

url = "https://api.github.com"
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    print("GET запрос успешно выполнен:")
    print(response.json())
except requests.RequestException as e:
    print("Ошибка при выполнении GET запроса:", e)
print("-" * 40)
```

**Что делает:**
- Отправка GET-запроса к GitHub API
- Вывод JSON-ответа

**Методы:**
- `requests.get(url)` — отправка запроса.
- `response.json()` — распарсенный JSON-объект.

---

### 2. Выполнение POST-запроса с JSON-данными

```python
import requests

url = "https://httpbin.org/post"
payload = {"username": "test_user", "password": "secret"}
try:
    response = requests.post(url, json=payload, timeout=5)
    response.raise_for_status()
    print("POST запрос успешно выполнен:")
    print(response.json())
except requests.RequestException as e:
    print("Ошибка при выполнении POST запроса:", e)
```

**Что делает:**
- Отправляет POST-запрос на `httpbin.org`.
- Передаёт словарь данных в теле запроса в формате JSON.
- Выводит ответ от сервера.

**Методы:**
- `requests.post(url, json=payload)` — отправка JSON в теле запроса.
- `response.json()` — парсинг полученного ответа.

---

### 3. Использование кастомных заголовков

```python
import requests

url = "https://api.github.com"
headers = {
    "User-Agent": "MyApp/1.0",
    "Accept": "application/vnd.github.v3+json"
}
try:
    response = requests.get(url, headers=headers, timeout=5)
    response.raise_for_status()
    print("GET запрос с кастомными заголовками успешно выполнен:")
    print(response.json())
except requests.RequestException as e:
    print("Ошибка при выполнении запроса с заголовками:", e)
```

**Что делает:**
- Отправляет GET-запрос на `https://api.github.com` с собственными заголовками.

**Методы:**
- `requests.get(url, headers={...})` — добавление query-параметров.
- `response.json()` — извлечение списка объектов (комментариев).


## Как запустить примеры

Запустить примеры можно следующим образом:

```bash
py src/libraries/requests_example.py
```

---

## Исходный код

Доступен в файле [src/libraries/requests_example.py](../../src/libraries/requests_example.py)
