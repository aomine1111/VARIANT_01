def selection_sort(arr):
    """
    Функция сортировки выбором (Selection Sort).
    На каждом шаге находит минимальный элемент и ставит его в начало списка.
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == '__main__':
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный список:", sample_list)
    sorted_list = selection_sort(sample_list.copy())
    print("Отсортированный список:", sorted_list)
