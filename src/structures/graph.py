class Graph:
    """
    Класс Graph реализует неориентированный граф с использованием списков смежности.
    """

    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """Добавляет вершину в граф."""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, v1, v2):
        """
        Добавляет ребро между вершинами v1 и v2.
        Для неориентированного графа добавляем ребро в обе стороны.
        """
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.adjacency_list[v1].append(v2)
        self.adjacency_list[v2].append(v1)

    def get_neighbors(self, vertex):
        """Возвращает список смежных вершин для данной вершины."""
        return self.adjacency_list.get(vertex, [])

    def __str__(self):
        return '\n'.join(f'{vertex}: {neighbors}' for vertex, neighbors in self.adjacency_list.items())

if __name__ == '__main__':
    # Пример использования графа
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "D")
    print("Граф:")
    print(graph)
