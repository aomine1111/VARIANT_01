# Pytest

Pytest позволяет удобно писать тесты для Python кода, включая параметризованные тесты и использование фикстур.

**Исходный файл с примерами:**
[pytest_example.py](../../src/frameworks/pytest_example.py)

---

## Структура примеров

### 1. Тестирование функции сложения
- Функция `add(a, b)` возвращает сумму двух чисел.
- Тест проверяет корректность работы функции на различных наборах данных.

```python
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
```

---

### 2. Параметризованные тесты для умножения
- Использование декоратора `@pytest.mark.parametrize` для проверки функции умножения с различными входными значениями.

```python
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-1, 5, -5),
    (0, 99, 0),
    (7, 7, 49)
])
def test_multiply(a, b, expected):
    assert a * b == expected
```

---

### 3. Тест с использованием фикстуры
- Фикстура `sample_list` предоставляет список чисел.
- Тест проверяет, что сумма элементов списка равна ожидаемому значению.

```python
@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

def test_sum(sample_list):
    assert sum(sample_list) == 15
```

---

## Запуск тестов

Убедитесь, что библиотека pytest установлена:

```bash
pip install pytest
```

Для запуска тестов выполните:
```bash
pytest test_example.py
```

