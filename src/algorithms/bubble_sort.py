def bubble_sort(arr):
    """
    Функция сортировки пузырьком (Bubble Sort).
    Проходит по списку, сравнивая и меняя местами соседние элементы,
    пока список не будет отсортирован.
    """
    n = len(arr)
    # Повторяем проходы по списку
    for i in range(n):
        # Последние i элементов уже на своих местах
        for j in range(0, n - i - 1):
            # Если текущий элемент больше следующего, меняем их местами
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == '__main__':
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный список:", sample_list)
    sorted_list = bubble_sort(sample_list.copy())
    print("Отсортированный список:", sorted_list)
