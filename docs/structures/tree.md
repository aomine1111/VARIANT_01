# Бинарное дерево (Binary Tree)

**Бинарное дерево** — структура данных, где каждый узел имеет не более двух потомков: левый и правый.

## Основные методы

- **insert_left(node, data)** – вставляет элемент в левое поддерево.
- **insert_right(node, data)** – вставляет элемент в правое поддерево.
- **inorder_traversal(node)** – симметричный (in-order) обход дерева.

## Пример использования

```python
from src.structures.tree import BinaryTree

if __name__ == '__main__':
    bt = BinaryTree(10)
    bt.insert_left(bt.root, 5)
    bt.insert_right(bt.root, 15)
    bt.insert_left(bt.root.left, 3)
    bt.insert_right(bt.root.left, 7)
    print("In-order обход дерева:", bt.inorder_traversal(bt.root)) # [3, 5, 7, 10, 15]
```

## Исходный код
Код структуры данных находится в [/src/structures/tree.py](../../src/structures/tree.py)