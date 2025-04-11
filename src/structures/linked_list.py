# linked_list.py

class Node:
    """Класс Node представляет узел связного списка."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    Класс LinkedList реализует односвязный список.
    """

    def __init__(self):
        self.head = None

    def append(self, data):
        """Добавляет новый узел с данными в конец списка."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Добавляет новый узел в начало списка."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """Удаляет первый найденный узел с данными равными key."""
        current = self.head
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next
        if current is None:
            return  # элемент не найден
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def display(self):
        """Выводит элементы списка."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

if __name__ == '__main__':
    # Пример использования связного списка
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.prepend(5)
    print("Элементы списка:", ll.display())
    ll.delete(10)
    print("После удаления элемента 10:", ll.display())
