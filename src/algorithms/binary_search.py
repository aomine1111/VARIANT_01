def binary_search(arr, target):
    """
    Функция бинарного поиска в отсортированном списке.
    Если target найден, возвращает его индекс, иначе возвращает -1.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  # Находим средний индекс
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Ищем в правой половине
        else:
            right = mid - 1  # Ищем в левой половине
    return -1

if __name__ == '__main__':
    # Пример: список должен быть отсортирован
    sorted_list = [1, 3, 5, 7, 9, 11]
    target = 7
    index = binary_search(sorted_list, target)
    print(f"Индекс элемента {target} в списке: {index}")
