# Pydantic

В данном документе описаны примеры использования библиотеки **Pydantic** для валидации и сериализации данных. Pydantic позволяет создавать модели данных с автоматической валидацией на основе аннотаций типов.

**Исходный файл с примерами:**  
[pydantic_example.py](../../src/frameworks/pydantic_example.py)

---

## Структура примеров

### 1. Модель данных User
- Определяет модель пользователя с полями: `id`, `name`, `email` и опциональное поле `age`.
- Для каждого поля заданы ограничения (например, `id` должен быть положительным, `email` соответствует формату).

```python
class User(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=2, max_length=50)
    email: str = Field(..., pattern=r'^\S+@\S+\.\S+$')
    age: Optional[int] = Field(None, ge=18, le=99)
```

---

### 2. Демонстрация работы модели
- Создание экземпляра модели с корректными данными.
- Попытка создать экземпляр с некорректными данными приводит к ошибке валидации.
- Сериализация корректного объекта в JSON для удобного отображения.

```python
def main():
    try:
        user = User(id=1, name="Nikita", email="MrJFgaming@yandex.com", age=30)
        print("Создан пользователь:", user)
        
        invalid_user = User(id=-1, name="И", email="invalid-email", age=17)
    except ValidationError as e:
        print("Ошибка валидации:", e)
    
    print("JSON представление пользователя:", user.model_dump_json(indent=4))
```

---

## Запуск

Убедитесь, что библиотека Pydantic установлена:

```bash
pip install pydantic
```

Для запуска примера выполните:

```bash
py pydantic_example.py
```


