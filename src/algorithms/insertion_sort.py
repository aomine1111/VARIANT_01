def insertion_sort(arr):
    """
    Функция сортировки вставками (Insertion Sort).
    Постепенно строит окончательный отсортированный список,
    вставляя каждый новый элемент в нужное место.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Перемещаем элементы массива, которые больше key, на одну позицию вправо
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == '__main__':
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный список:", sample_list)
    sorted_list = insertion_sort(sample_list.copy())
    print("Отсортированный список:", sorted_list)
