from pydantic import BaseModel, Field, ValidationError
from typing import Optional


class User(BaseModel):
    """
    Модель пользователя с валидацией данных.
    """
    id: int = Field(..., gt=0, description="Уникальный идентификатор пользователя")
    name: str = Field(..., min_length=2, max_length=50, description="Имя пользователя")
    email: str = Field(..., pattern=r'^\S+@\S+\.\S+$', description="Email пользователя")
    age: Optional[int] = Field(None, ge=18, le=99, description="Возраст пользователя")

def main():
    """
    Основная функция для демонстрации работы Pydantic.
    """
    try:
        # Создание экземпляра User с корректными данными
        user = User(id=1, name="Иван", email="MrJFgaming@yandex.com", age=30)
        print("Создан пользователь:", user)

        # Попытка создания пользователя с некорректными данными
        invalid_user = User(id=-1, name="И", email="invalid-email", age=17)
    except ValidationError as e:
        print("Ошибка валидации:", e)

    # Сериализация пользователя в JSON
    print("JSON представление пользователя:", user.model_dump_json(indent=4))

if __name__ == "__main__":
    main()
