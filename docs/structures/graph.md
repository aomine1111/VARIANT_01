# Граф (Graph)

**Граф** — структура данных, состоящая из вершин и рёбер, соединяющих их. В нашем примере используется неориентированный граф, реализованный на основе списков смежности.

## Основные методы

- **add_vertex(vertex)** – добавляет вершину в граф.
- **add_edge(v1, v2)** – добавляет ребро между вершинами.
- **get_neighbors(vertex)** – возвращает список смежных вершин.

## Пример использования

```python
from src.structures.graph import Graph

if __name__ == '__main__':
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "D")
    print("Граф:")
    print(graph)
    # A: ['B', 'C']
    # B: ['A', 'D']
    # C: ['A', 'D']
    # D: ['B', 'C']
```

## Исходный код
Код структуры данных находится в [/src/structures/graph.py](../../src/structures/graph.py)