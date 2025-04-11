# Очередь (Queue)

**Очередь** – структура данных по принципу FIFO (First In, First Out). Первый добавленный элемент извлекается первым.

## Основные методы

- **is_empty()** – проверяет, пуста ли очередь.
- **enqueue(item)** – добавляет элемент в конец очереди.
- **dequeue()** – извлекает элемент из начала очереди.
- **size()** – возвращает число элементов в очереди.

## Пример использования

```python
from src.structures.queue import Queue

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    print("Извлечённый элемент:", queue.dequeue()) # 10
    print("Размер очереди:", queue.size()) # 1
```

## Исходный код
Код структуры данных находится в [/src/structures/queue.py](../../src/structures/queue.py)