class HashTable:
    """
    Простейшая реализация хеш-таблицы с использованием метода открытой адресации (линейное пробирование).
    """

    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):
        """Простая хеш-функция для строковых и числовых ключей."""
        return hash(key) % self.size

    def put(self, key, value):
        """Добавляет пару ключ-значение в хеш-таблицу."""
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("Хеш-таблица заполнена")
        self.table[index] = (key, value)

    def get(self, key):
        """Возвращает значение по ключу. Если ключ не найден, возвращает None."""
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                break
        return None

    def delete(self, key):
        """Удаляет пару ключ-значение по ключу."""
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return
            index = (index + 1) % self.size
            if index == original_index:
                break

if __name__ == '__main__':
    # Пример использования хеш-таблицы
    ht = HashTable()
    ht.put("apple", 100)
    ht.put("banana", 200)
    print("Значение для 'apple':", ht.get("apple"))
    ht.delete("apple")
    print("После удаления 'apple':", ht.get("apple"))
