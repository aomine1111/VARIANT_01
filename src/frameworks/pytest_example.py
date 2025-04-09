import pytest

# Функция для тестирования
def add(a: int, b: int) -> int:
    """
    Функция сложения двух чисел.
    """
    return a + b

# Тест для функции add
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# Параметризованный тест для функции умножения
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-1, 5, -5),
    (0, 99, 0),
    (7, 7, 49)
])
def test_multiply(a, b, expected):
    assert a * b == expected

# Фикстура для подготовки данных
@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

# Тест с использованием фикстуры
def test_sum(sample_list):
    assert sum(sample_list) == 15
