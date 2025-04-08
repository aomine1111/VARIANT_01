from collections import deque

def bfs(graph, start):
    """
    Функция поиска в ширину (BFS).
    Обходит граф, начиная с вершины start.
    """
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

if __name__ == '__main__':
    # Пример графа в виде словаря (связи между вершинами)
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    print("Обход графа в ширину, начиная с вершины A:")
    bfs(graph, 'A')
