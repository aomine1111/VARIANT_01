def linear_search(arr, target):
    """
    Функция линейного поиска (Linear Search).
    Перебирает все элементы списка для поиска заданного значения.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == '__main__':
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    target_value = 22
    result = linear_search(sample_list, target_value)
    if result != -1:
        print(f"Элемент {target_value} найден на позиции {result}.")
    else:
        print(f"Элемент {target_value} не найден.")
