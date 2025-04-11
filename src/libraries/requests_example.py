import requests

def example_get_request():
    """
    Пример GET запроса:
    - Отправка GET-запроса к публичному API (например, GitHub API)
    - Вывод JSON-ответа
    """
    url = "https://api.github.com"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        print("GET запрос успешно выполнен:")
        print(response.json())
    except requests.RequestException as e:
        print("Ошибка при выполнении GET запроса:", e)
    print("-" * 40)

def example_post_request():
    """
    Пример POST запроса:
    - Отправка POST-запроса к сервису для тестирования (httpbin.org)
    - Передача JSON-данных в теле запроса и вывод ответа
    """
    url = "https://httpbin.org/post"
    payload = {"username": "test_user", "password": "secret"}
    try:
        response = requests.post(url, json=payload, timeout=5)
        response.raise_for_status()
        print("POST запрос успешно выполнен:")
        print(response.json())
    except requests.RequestException as e:
        print("Ошибка при выполнении POST запроса:", e)
    print("-" * 40)

def example_custom_headers():
    """
    Пример использования кастомных заголовков:
    - Отправка GET запроса с дополнительными заголовками
    """
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
    print("-" * 40)

if __name__ == '__main__':
    print("=== Примеры работы с Requests ===\n")
    example_get_request()
    example_post_request()
    example_custom_headers()
