
# FastAPI

В данном документе описаны примеры кода для демонстрации возможностей фреймворка **FastAPI**. FastAPI — это современный, быстрый (high-performance) веб-фреймворк для Python, использующий стандартные Python-аннотации типов и асинхронное программирование. Он предназначен для создания API, автоматически генерируя документацию по его эндпоинтам (например, Swagger UI).

**Исходный файл с примерами:**  
[fastapi_example.py](../../src/frameworks/fastapi_example.py)

**URL для тестирования:**  
Приложение запускается локально, по умолчанию доступно по http://127.0.0.1:8000  
Для просмотра интерактивной документации можно перейти по http://127.0.0.1:8000/docs

---

## Структура примеров

В файле `fastapi_example.py` реализовано 5 примеров, которые демонстрируют различные возможности FastAPI:

---

### 1. Корневой эндпоинт  
Возвращает JSON с приветственным сообщением для проверки работоспособности API.  

```python
@app.get("/")
async def read_root():
   return {"message": "Добро пожаловать в FastAPI!"}
```

---

### 2. Эндпоинт с параметром пути
При обращении к URL `/users/{user_id}` передаётся параметр `user_id`, и возвращается информация о пользователе.

```python
@app.get("/users/{user_id}")
async def read_user(user_id: int):
   return {"user_id": user_id, "name": f"Пользователь {user_id}"}
```

---

### 3. Эндпоинт с параметрами запроса
Обращение к `/users` с параметрами `skip` и `limit` для реализации пагинации возвращает список пользователей.  

```python
@app.get("/users")
async def get_users(skip: int = 0, limit: int = 10):
   users = [{"user_id": i, "name": f"Пользователь {i}"} for i in range(skip, skip + limit)]
   return {"users": users}
```

---

### 4. Эндпоинт с обработкой ошибок
При запросе к `/items/{item_id}` проверяется корректность `item_id`. Если значение некорректно (<= 0), возвращается ошибка 404.

```python
@app.get("/items/{item_id}")
async def read_item(item_id: int):
   if item_id <= 0:
       raise HTTPException(status_code=404, detail="Товар не найден")
   return {"item_id": item_id, "description": f"Описание товара с идентификатором {item_id}"}
```

---

### 5. Демонстрация асинхронной работы
Эндпоинт `/async-demo` имитирует длительную операцию с помощью `asyncio.sleep`, демонстрируя возможности асинхронного программирования.  

```python
@app.get("/async-demo")
async def async_demo():
   await asyncio.sleep(1)
   return {"status": "Операция завершена успешно"}
```