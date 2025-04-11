class Stack:
    """
    Класс Stack реализует структуру данных «стек».
    Принцип работы: последний пришёл — первый ушёл (LIFO).
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        """Возвращает True, если стек пуст."""
        return len(self.items) == 0

    def push(self, item):
        """Добавляет элемент в стек."""
        self.items.append(item)

    def pop(self):
        """Извлекает последний элемент из стека."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Возвращает последний элемент стека, не удаляя его."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        """Возвращает количество элементов в стеке."""
        return len(self.items)

if __name__ == '__main__':
    # Пример использования стека
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print("Верхний элемент:", stack.peek())
    print("Извлечённый элемент:", stack.pop())
    print("Размер стека:", stack.size())
