# Связный список (Linked List)

**Связный список** — последовательность узлов, где каждый узел содержит данные и ссылку на следующий элемент.

## Основные методы

- **append(data)** – добавляет элемент в конец списка.
- **prepend(data)** – добавляет элемент в начало списка.
- **delete(key)** – удаляет узел с определёнными данными.
- **display()** – возвращает список всех элементов.

## Пример использования

```python
from src.structures.linked_list import LinkedList

if __name__ == '__main__':
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.prepend(5)
    print("Элементы списка:", ll.display()) # [5, 10, 20]
    ll.delete(10)
    print("После удаления элемента 10:", ll.display()) # [5, 20]
```

## Исходный код
Код структуры данных находится в [/src/structures/linked_list.py](../../src/structures/linked_list.py)